from django import forms
from .models import (
    ATC,
    Language,
    Presentation,
    ActiveIngredient
)
from apps.presentation.models import Language as language


class LanguageForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.Select(choices=language.objects.all().values_list('id', 'name')))
                                                   
    class Meta:
        model = Language
        fields = ('product_listing_file', 'pricing_file','name')
    
    
    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)

        # if 'product_listing_file' in self.changed_data or 'pricing_file' in self.changed_data:
        #     self.instance.process()

        # elif 'atc_file' in self.changed_data: pass

        # elif 'presentation_file' in self.changed_data: pass
        print(self.changed_data)
        super().save(*args, **kwargs)
        self.instance.process()


class ATCForm(forms.ModelForm):
    class Meta:
        model = ATC
        fields = ("file",)

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ("file",)


class ActiveIngredientForm(forms.ModelForm):
    class Meta:
        model = ActiveIngredient
        fields = ("file",)