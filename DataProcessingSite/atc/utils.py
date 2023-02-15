from presentation.models import Language
from atc.models import Atc, AtcLanguage
from main.csv_xl import FileReader
from lxml import etree
from xml.etree import ElementTree
import uuid
import os
import pandas as pd


class ReadAtcCsvAndSaveInDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dataframe()
        self.extract_rows()
        self.save_in_database()

    def file_dataframe(self):
        fr = FileReader(self.file_path, output_filename=self.file_path)
        self.filereader = fr
        self.dataframe = fr.dataframe

    def etree_tostring(self, tree):
        return etree.tostring(tree, pretty_print=True).decode()

    def extract_rows(self):
        ''' get tr table rows fro generated html string'''
        t = self.file_to_html()
        rows = etree.HTML(t).findall(".//tr")
        rows = [self.etree_tostring(i) for i in rows]
        self.header = rows[0]
        self.rows = rows[1:]

    def file_to_html(self):
        self.file_dataframe()
        df = self.dataframe.loc[:]
        return df.to_html(classes=['table', 'table-hover', 'table-bordered'])

    def save_in_database(self):
        header = ElementTree.fromstring(self.header)
        for pos, head in enumerate(header):
            if head.text:
                for row in self.rows:
                    row = ElementTree.fromstring(row)
                    atc = row[1].text
                    language = head.text
                    if language.lower() != 'atc':
                        name = row[pos].text
                        if name is not None and name != '' and name != 'NaN':
                            atc, _ = Atc.objects.get_or_create(atc_code=atc)
                            language, _ = Language.objects.get_or_create(name=language)
                            AtcLanguage.objects.get_or_create(
                                atc=atc, language=language, name=name
                            )

    def __str__(self):
        return self.file_path