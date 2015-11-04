from django.shortcuts import render_to_response, get_object_or_404
from app.ayarlar.models import *
from django.template.response import TemplateResponse
from django.template import RequestContext
from app.hakkimizda.models import *

def HakkimizdaView(request):
    hakkimizda=Hakkimizda.objects.all()
    yoneticiler=Yoneticilerimiz.objects.all()
    ayar=Ayarlar.objects.all()
    sosyal=SosyalMedya.objects.all()
    referans=Referanslar.objects.all()
    ctx={'hakkimizda':hakkimizda,'ayar':ayar,'yoneticiler':yoneticiler,'referans':referans,'sosyal':sosyal}
    return render_to_response("hakkimizda.html", ctx)
