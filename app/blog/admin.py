from django.contrib import admin
from app.blog.models import Kategori, Makale
from django.db.models import TextField
from app.tinymce.models import *
from django.conf import settings
#from django_filepicker.wymeditor.widgets import WYMeditorWidget

class MakaleAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('baslik',)}
    list_display= ('baslik','yayin_tarihi','kategori')
    search_fields=['baslik']
    class Media:
        js=(settings.STATIC_URL+'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL+'js/tiny_mce/textareas.js',)
   # formfield_overrides= { TextField: {'widget':WYMeditorWidget({})}}
    #class Media:
     #   js= ('http://cdn.jquerytools.org/1.2.7/full/jquery.tools.min.js',)

class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('baslik',)}

#class YazarAdmin(admin.ModelAdmin):
#    prepopulated_fields= {'slug': ('isim',)}

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Makale, MakaleAdmin)
#admin.site.register(Yazar,YazarAdmin)
