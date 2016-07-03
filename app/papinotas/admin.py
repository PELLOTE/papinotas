from django.contrib import admin
from app.papinotas.models import *
# Register your models here.
class GroupsAdmin(admin.ModelAdmin): 
    list_display = ('name', 'group_type', 'student_counter', 'has_changes')
    search_fields = ['group_type','name']
admin.site.register(Groups, GroupsAdmin)

class StudentsAdmin(admin.ModelAdmin): 
    list_display = ('name', 'self', 'ap1', 'ap2')
    search_fields = ['name']
admin.site.register(Students, StudentsAdmin)
