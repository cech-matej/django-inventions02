from django.contrib import admin
from .models import *

from django.db.models import Count
from django.utils.html import format_html

# Register your models here.
admin.site.register(Nation)
admin.site.register(Category)
admin.site.register(Inventor)
admin.site.register(Invention)


# @admin.register(Nation)
# class NationAdmin(admin.ModelAdmin):
#     list_display = ("abbr", "name")
