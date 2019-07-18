from django.contrib import admin
from django import forms
from .models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
