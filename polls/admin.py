from django.contrib import admin

# Register your models here.
from .models import Question, Name

admin.site.register(Question)
admin.site.register(Name)