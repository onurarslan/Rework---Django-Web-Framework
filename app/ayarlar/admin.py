from django.contrib import admin
from app.ayarlar.models import *
from django.conf import settings

class AyarlarAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slugBaslik": ("siteBaslik",)}

class MansetAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("mansetBaslik",)}

admin.site.register(Ayarlar, AyarlarAdmin)
admin.site.register(Manset,MansetAdmin)
admin.site.register(Referanslar)
admin.site.register(SosyalMedya)
