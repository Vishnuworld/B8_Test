from django.contrib import admin
from .models import *
admin.ModelAdmin
# Register your models here.
from django.contrib.admin.models import LogEntry

# admin.site.register([Person, College, Principal, Department, Student, Subject])



@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print("hi hello")
        super().save_model(request, obj, form, change)