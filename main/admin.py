from django import forms
from django.contrib import admin

# Register your models here.
from .models import *


class GradeInline(admin.TabularInline):
    model = Grade
    raw_id_fields = ['students']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['teachers', 'name']
    inlines = [GradeInline]


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Teach, GradeAdmin)
