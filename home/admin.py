from django.contrib import admin

# Register your models here.
from . models import customer,resume
admin.site.register(customer)
admin.site.register(resume)