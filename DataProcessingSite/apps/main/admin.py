from django.contrib import admin
from .models import (
    ATC,
    Language,
    Presentation,
    ActiveIngredient,
    ATC_Entry,
    Presentation_Entry
)


class ATCAdmin(admin.ModelAdmin):
    pass
admin.site.register(ATC, ATCAdmin)


class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class PresentationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Presentation, PresentationAdmin)

class ActiveIngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(ActiveIngredient, ActiveIngredientAdmin)


class ATC_EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ATC_Entry, ATC_EntryAdmin)

class Presentation_EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Presentation_Entry, Presentation_EntryAdmin)
