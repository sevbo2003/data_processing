from django.db import models
from main.models import Presentation
from main.csv_xl import FileReader
from lxml import etree
from xml.etree import ElementTree
import uuid
import os
import pandas as pd


class EnglishName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "English Names"
        ordering = ['id']


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Languages"
        ordering = ['id']


class PresentationLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    english_name = models.ForeignKey(EnglishName, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Presentation Languages"
        ordering = ['id']