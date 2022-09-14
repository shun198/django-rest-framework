from django.contrib import admin
from .models import Place, Restaurant, Reporter, Article, Publication, Fruits

# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Fruits)
