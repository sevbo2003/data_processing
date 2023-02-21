import uuid
from django.db import models
from lxml import etree
from apps.main.csv_xl import FileReader
import os

from django.conf import settings
from apps.presentation.models import Language


def csv_column_names():
    return ['name', 'eu_code', 'national_registration_number', 'date_of_registration', 'registration_expiration',
            'description', 'atc_code', 'ma_holder', 'prescription_status', 'link_to_spc', 'link_to_pil',
            'reimbursement', 'pack_size', 'presentation', 'route', 'is_commercial', 'is_narcotic',
            'active_ingredient_1', 'active_ingredient_2', 'active_ingredient_3', 'active_ingredient_4',
            'strength_1', 'strength_2', 'strength_3', 'strength_4']


class Product(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=500, blank=True, null=True)
    eu_code = models.CharField(max_length=500, blank=True, null=True)
    national_registration_number = models.CharField(max_length=500, blank=True, null=True)
    date_of_registration = models.CharField(max_length=500 ,blank=True, null=True)
    registration_expiration = models.CharField(max_length=500 ,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    atc_code = models.CharField(max_length=500)
    ma_holder = models.CharField(max_length=500, blank=True, null=True)
    prescription_status = models.CharField(max_length=500, blank=True, null=True)
    link_to_spc = models.CharField(max_length=500, blank=True, null=True)
    link_to_pil = models.CharField(max_length=500, blank=True, null=True)
    reimbursement = models.CharField(max_length=500, blank=True, null=True)
    pack_size = models.CharField(max_length=500, blank=True, null=True)
    presentation = models.CharField(max_length=500, blank=True, null=True)
    atc = models.CharField(max_length=500, blank=True, null=True)
    route = models.CharField(max_length=500, blank=True, null=True)
    is_commercial = models.BooleanField(default=False, blank=True, null=True)
    is_narcotic = models.BooleanField(default=False, blank=True, null=True)
    active_ingredient_1 = models.CharField(max_length=500, blank=True, null=True)
    active_ingredient_2 = models.CharField(max_length=500, blank=True, null=True)
    active_ingredient_3 = models.CharField(max_length=500, blank=True, null=True)
    active_ingredient_4 = models.CharField(max_length=500, blank=True, null=True)
    strength_1 = models.CharField(max_length=500, blank=True, null=True)
    strength_2 = models.CharField(max_length=500, blank=True, null=True)
    strength_3 = models.CharField(max_length=500, blank=True, null=True)
    strength_4 = models.CharField(max_length=500, blank=True, null=True)
