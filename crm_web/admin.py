from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('fio', 'address', 'revenue')
    list_display_link = ('fio', 'address', 'revenue')
