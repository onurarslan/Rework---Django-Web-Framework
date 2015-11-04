from django.shortcuts import render_to_response, get_object_or_404
from app.ttk.models import *
from app.ayarlar.models import *
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.db.models import Sum

def ticaretSicilBilgileri(request):
    tsb=TicaretSicilBilgileri.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'tsb':tsb,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "ttk.html", ctx)

def ortaklikYapisi(request):
    oy=OrtaklikYapisi.objects.all()
    toplamCiro=OrtaklikYapisi.objects.aggregate(Sum('ortakCiro'))
    toplamYuzde=OrtaklikYapisi.objects.aggregate(Sum('ortakYuzde'))
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'oy':oy,'toplamCiro':toplamCiro,'toplamYuzde':toplamYuzde,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "ortaklikYapisi.html", ctx)
    
def yonetimKurulu(request):
    yk=YonetimKurulu.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'yk':yk,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "yonetimKurulu.html", ctx)

def denetciler(request):
    denetci=Denetciler.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'denetci':denetci,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "denetciler.html", ctx)

def ustYonetim(request):
    uy=UstYonetim.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'uy':uy,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "ustYonetim.html", ctx)

def donemselFinans(request):
    df=DonemselFinansalSonuclar.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'df':df,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "donemselFinans.html", ctx)

def faaliyetRaporlari(request):
    fr=FaaliyetRaporlari.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'fr':fr,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "faaliyetRaporlari.html", ctx)

def genelKurulBilgileri(request):
    gk=GenelKurulBilgileri.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'gk':gk,'sosyal':sosyal,'ayar':ayar}
    return TemplateResponse(request, "genelKurul.html", ctx)
