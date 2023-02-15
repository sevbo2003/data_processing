from django import forms
from .models import (
    ATC,
    Language,
    Presentation,
    ActiveIngredient
)


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('product_listing_file', 'pricing_file',)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if 'product_listing_file' in self.changed_data or 'pricing_file' in self.changed_data:
            self.instance.process()

        elif 'atc_file' in self.changed_data: pass

        elif 'presentation_file' in self.changed_data: pass

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