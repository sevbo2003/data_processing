from django.contrib import admin
from .models import *


class AtcAdmin(admin.ModelAdmin):
    list_display = ('atc_code',)
    search_fields = ('atc_code',)
    list_filter = ('atc_code',)
    ordering = ('atc_code',)

admin.site.register(Atc, AtcAdmin)
