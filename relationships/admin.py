from django.contrib import admin
from relationships import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Book)
admin.site.register(models.Workplace)
admin.site.register(models.Bank)
