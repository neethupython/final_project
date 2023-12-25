# core/admin.py
from django.contrib import admin
from .models import Department, Course,Material,FormModel,UserProfile

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(FormModel)
admin.site.register(UserProfile)