from django.contrib import admin
from .models import Customer,Entry,Goal
# Register your models here.
admin.site.register(Customer)
admin.site.register(Entry)
admin.site.register(Goal)