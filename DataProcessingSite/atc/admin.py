from django.contrib import admin
from .models import *


class AtcAdmin(admin.ModelAdmin):
    list_display = ('atc_code',)
    search_fields = ('atc_code',)
    list_filter = ('atc_code',)
    ordering = ('atc_code',)

admin.site.register(Atc, AtcAdmin)


class AtcLanguageAdmin(admin.ModelAdmin):
    list_display = ('atc', 'language', 'name')
    search_fields = ('atc__atc_code', 'language__name', 'name')
    list_filter = ('atc', 'language', 'name')
    ordering = ('atc', 'language', 'name')

admin.site.register(AtcLanguage, AtcLanguageAdmin)