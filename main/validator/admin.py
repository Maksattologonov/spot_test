from django.contrib import admin

from .models import Formula


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    pass
