from django.contrib import admin
from rkmkapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list = ['Name','Email','Subject','Message']

admin.site.register(Student, StudentAdmin)
