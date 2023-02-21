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
