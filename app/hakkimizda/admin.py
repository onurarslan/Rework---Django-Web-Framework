from django.contrib import admin
from django.conf import settings
from app.hakkimizda.models import *

class HakkimizdaAdmin(admin.ModelAdmin):
    class Media:
        js=(settings.STATIC_URL+'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL+'js/tiny_mce/textareas.js',)

admin.site.register(Hakkimizda,HakkimizdaAdmin)
admin.site.register(Yoneticilerimiz)
