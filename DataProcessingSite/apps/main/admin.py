from django.contrib import admin
from .models import (
    ATC,
    Language,
    Presentation,
    ActiveIngredient
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
