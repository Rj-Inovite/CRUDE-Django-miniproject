from django.contrib import admin

# Register your models here.
import crud.models
admin.site.register(crud.models.customer)   
