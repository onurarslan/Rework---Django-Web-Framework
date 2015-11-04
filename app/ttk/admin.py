from django.contrib import admin
from app.ttk.models import *
from django.db.models import TextField
from app.tinymce.models import *
from django.conf import settings

class TicSicBilgAdmin(admin.ModelAdmin):
    list_display= ('unvan','kurulusTarihi','ticaretSicilNo','tescilTarihi')

class OrtYapAdmin(admin.ModelAdmin):
    list_display=('ortak','ortakCiro','ortakYuzde')

class YonKurAdmin(admin.ModelAdmin):
    list_display=('gorevi','adiSoyadi')
    
class UstYonetimAdmin(admin.ModelAdmin):
    list_display=('gorevi','adiSoyadi')

admin.site.register(TicaretSicilBilgileri, TicSicBilgAdmin)
admin.site.register(OrtaklikYapisi, OrtYapAdmin)
admin.site.register(YonetimKurulu, YonKurAdmin)
admin.site.register(Denetciler)
admin.site.register(UstYonetim,UstYonetimAdmin)
admin.site.register(DonemselFinansalSonuclar)
admin.site.register(FaaliyetRaporlari)
admin.site.register(GenelKurulBilgileri)
