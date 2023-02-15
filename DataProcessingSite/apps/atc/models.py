from django.db import models
from apps.presentation.models import Language


class Atc(models.Model):
    atc_code = models.CharField(max_length=100)

    def __str__(self):
        return self.atc_code

    class Meta:
        verbose_name_plural = "ATC"
        ordering = ['atc_code']


class AtcLanguage(models.Model):
    atc = models.ForeignKey(Atc, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ATC Languages"
        ordering = ['atc']
        