from django.contrib import admin

from .models import *
from django.contrib.auth.models import Permission
# Register your models here.



admin.site.register(Course)
admin.site.register(Permission)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Project_experience)