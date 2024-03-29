from django.contrib import admin
from .models import *


class EnglishNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(EnglishName, EnglishNameAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Language, LanguageAdmin)


class PresentationLanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'english_name', 'name')
    search_fields = ('language', 'english_name', 'name')
    list_per_page = 25

admin.site.register(PresentationLanguage, PresentationLanguageAdmin)