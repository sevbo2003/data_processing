import uuid
from django.db import models
from lxml import etree
from .csv_xl import FileReader
import os


def user_directory_path(instance, filename):
    model_name = instance._meta.model.__name__
    return '{0}/{1}'.format(model_name, filename)


class ATC(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=user_directory_path)
    last_updated = models.DateTimeField(auto_now=True)

    def file_dataframe(self):
        fr = FileReader(self.file.path, output_filename=self.file.path)
        self.filereader = fr
        self.dataframe = fr.dataframe

    def etree_tostring(self, tree):
        return etree.tostring(tree, pretty_print=True).decode()

    def extract_rows(self):
        ''' get tr table rows fro generated html string'''
        t = self.file_to_html()
        rows = etree.HTML(t).findall(".//tr")
        rows = [self.etree_tostring(i) for i in rows]
        return rows[0], rows[1:]

    def file_to_html(self):
        self.file_dataframe()
        # df = self.dataframe.loc[:, 'ATC':'Name']
        df = self.dataframe.loc[:]
        # df = pd.DataFrame(df)
        return df.to_html(classes=['table', 'table-hover', 'table-bordered'])

    class Meta:
        verbose_name_plural = "ATC"


class Presentation(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=user_directory_path)
    last_updated = models.DateTimeField(auto_now=True)

    def file_dataframe(self):
        fr = FileReader(self.file.path, output_filename=self.file.path)
        self.filereader = fr
        self.dataframe = fr.dataframe

    def etree_tostring(self, tree):
        return etree.tostring(tree, pretty_print=True).decode()

    def extract_rows(self):
        ''' get tr table rows fro generated html string'''
        t = self.file_to_html()
        rows = etree.HTML(t).findall(".//tr")
        rows = [self.etree_tostring(i) for i in rows]
        return rows[0], rows[1:]

    def file_to_html(self):
        self.file_dataframe()
        # df = self.dataframe.loc[:, 'ATC':'Name']
        df = self.dataframe.loc[:]
        # df = pd.DataFrame(df)
        return df.to_html(classes=['table', 'table-hover', 'table-bordered'])


class ActiveIngredient(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=user_directory_path)
    last_updated = models.DateTimeField(auto_now=True)

    def file_dataframe(self):
        fr = FileReader(self.file.path, output_filename=self.file.path)
        self.filereader = fr
        self.dataframe = fr.dataframe

    def etree_tostring(self, tree):
        return etree.tostring(tree, pretty_print=True).decode()

    def extract_rows(self):
        ''' get tr table rows fro generated html string'''
        t = self.file_to_html()
        rows = etree.HTML(t).findall(".//tr")
        rows = [self.etree_tostring(i) for i in rows]
        return rows[0], rows[1:]

    def file_to_html(self):
        self.file_dataframe()
        # df = self.dataframe.loc[:, 'ATC':'Name']
        df = self.dataframe.loc[:]
        # df = pd.DataFrame(df)
        return df.to_html(classes=['table', 'table-hover', 'table-bordered'])



class Language(models.Model):
    name = models.CharField(max_length=125)
    product_listing_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    pricing_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    atc_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    presentation_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    processed = models.BooleanField(default=False)
    output_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def output_filename(self,):
        file_source = self.product_listing_file or self.pricing_file
        name, ext = os.path.splitext(file_source)
        ext = ext if file_source else '.csv'
        return f"{self.name}_output" + ext

    def process(self):
        # read both files
        product_reader = FileReader(self.product_listing_file.path)
        product_df = product_reader.df
        price_reader = FileReader(self.pricing_file.path)
        price_df = price_reader.dataframe

        # combine dataframes
        combined_df = product_df.append([price_df])
        combined_df.to_csv(self.output_filename) if '.csv' in self.product_listing_file else combined_df.to_excel(self.output_filename)
        output_reader = FileReader(self.output_filename.path)
        output_df = output_reader.dataframe

        # registration numbers are in the first column
        reg_num_col = product_df.iloc[:, 1]

        # lookup active ingredients
        self.lookup_and_translate(output_reader, 'atc_code',
                                  'active_ingredient_1', ATC_Entry,
                                )
        
        # lookup presentation
        self.lookup_and_translate(output_reader, 'presentation',
                                  'presentation', Presentation_Entry,
                                )

        # save file
        output_reader.write_file()

    def lookup_and_translate(self, file_reader:FileReader, query_col, translate_col, model_query):
        file_reader.find_or_create_column(translate_col)
        df = file_reader.dataframe
        for ind in df.index:
            atc = df[query_col][ind]
            # look for this in ATC
            if model_query == ATC_Entry:
                translation = model_query.objects.filter(language="English", code=atc)
            else:
                translation = model_query.objects.filter(language="English", presentation=atc)
            translation = translation.first() if translation else file_reader.NULL_CELL
            file_reader.update_value(translate_col, ind)

    def update_ATC(self,):
        atc = ATC.objects.first()

        # iterate over rows in input file
        input_reader = FileReader(self.atc_file.path)
        df = input_reader.dataframe

        for ind in df.index:
            input_dict = {
                "ATC": df['atc_code'][ind],
                self.name: df.iloc[ind, 1],
            }
        self.update_file(self.atc_file, input_dict, ATC, 'ATC')

        atc.filereader.write_file()
        return

    def update_Presentations(self):
        presentation = Presentation.objects.first()
        input_dict = {
            "Presentation": self.presentation,
            self.language: self.name,
        }
        self.update_file(self.presentation_file, input_dict, presentation, self.language)
        presentation.filereader.write_file()
        return

    def update_file(self, input_dict, model_instance, column_name='ATC'):
        # update ATC/Presentations file whenever this is saved/updated
        file = model_instance.file
        model_instance.file_dataframe()

        # search for language in columns
        model_instance.filereader.find_or_create_column(self.name)

        # search for row 
        row = model_instance.filereader.query_by_column(column_name, self.code)

        # search for cell
        if row:
            model_instance.filereader.update_value(column_name, row, self.name)
        else:
            model_instance.filereader.new_row(input_dict)


    def __str__(self) -> str:
        return self.name


class ATC_Entry(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=20,)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Presentation_Entry(models.Model):
    name = models.CharField(max_length=500)
    presentation = models.CharField(max_length=20,)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)