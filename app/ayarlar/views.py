from app.ayarlar.models import *
from django.shortcuts import render_to_response,get_object_or_404
from django.template.response import TemplateResponse
from app.blog.models import *
from django.template import RequestContext
from app.hakkimizda.models import *
from app.portfolio.models import *

def ayarSite(request):
    ayar=Ayarlar.objects.all()
    sosyal=SosyalMedya.objects.all()
    hakkimizda=Hakkimizda.objects.all()
    return TemplateResponse(request, "base.html",{'hakkimizda':hakkimizda,'sosyal':sosyal,'ayar':ayar})
    #return render_to_response("base.html", locals())


def Index(request):
    makale=Makale.objects.all()
    ayar=Ayarlar.objects.all()
    manset=Manset.objects.all()
    referans=Referanslar.objects.all()
    sosyal=SosyalMedya.objects.all()
    hakkimizda=Hakkimizda.objects.all()
    portfolio=Portfolio.objects.all()
    return TemplateResponse(request, "index.html",{'portfolio':portfolio,'hakkimizda':hakkimizda,'sosyal':sosyal,'ayar':ayar,'makale':makale,'manset':manset,'referans':referans})

def MansetAc(request,slug):
    #manset=Manset.objects.all()
    manset=get_object_or_404(Manset, slug=slug)
    ayar=Ayarlar.objects.all()
    ctx={'manset':manset,'ayar':ayar}
    return TemplateResponse(request,"manset.html",ctx)
    #return render_to_response("manset.html", locals())
