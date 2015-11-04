from django.shortcuts import render_to_response, get_object_or_404
from app.ayarlar.models import *
from django.template.response import TemplateResponse
from django.template import RequestContext
from app.portfolio.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Kategoriler(request, slug):
    kategori=Kategori.objects.all()
    kategorim=get_object_or_404(Kategori, slug=slug)
    portfolio=Portfolio.objects.filter(kategori=kategorim)
    ayar=Ayarlar.objects.all()
    sosyal=SosyalMedya.objects.all()
    
    ctx={'portfolio':portfolio,'sosyal':sosyal,'kategori':kategori,'ayar':ayar}
    return TemplateResponse(request,"portfolio.html",ctx)
    #return render_to_response("kategoriBlog.html",locals())

def PortfolioGiris(request):
    portfolio=Portfolio.objects.all()
    ayar=Ayarlar.objects.all()
    kategori=Kategori.objects.all()
    sosyal=SosyalMedya.objects.all()
    ctx={'portfolio':portfolio,'kategori':kategori,'ayar':ayar,'sosyal':sosyal}
    return render_to_response("portfolio.html", ctx)

 
def PortfolioDetay(request, slug):
    portfolio=Portfolio.objects.all()
    ayar=Ayarlar.objects.all()
    kategori=Kategori.objects.all()
    sosyal=SosyalMedya.objects.all()
    sayfalama=Paginator(portfolio, 1)
    sayfaNo=request.GET.get('sayfam')
    portfolioDetay=get_object_or_404(Portfolio, slug=slug)
    try:
        sayfam=sayfalama.page(sayfaNo)
    except PageNotAnInteger:
        sayfam=sayfalama.page(1)
    except EmptyPage:
        sayfam=sayfalama.page(sayfalama.num_pages)
    
    
    ctx={'portfolioDetay':portfolioDetay,'kategori':kategori,'ayar':ayar,'sayfam':sayfam,'sosyal':sosyal}
    #return render_to_response(request,"portfolioDetay.html", ctx,context_instance=RequestContext(request))
    return TemplateResponse(request,"portfolioDetay.html",ctx)
