from django.db import models
from presentation.models import Language


class Atc(models.Model):
    atc_code = models.CharField(max_length=100)

    def __str__(self):
        return self.atc_code

    class Meta:
        verbose_name_plural = "ATC"
        ordering = ['atc_code']
