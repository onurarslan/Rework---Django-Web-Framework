from django.shortcuts import render_to_response, get_object_or_404
from app.blog.models import Kategori, Makale
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from app.ayarlar.models import *
from app.blog.forms import *
from django.template.response import TemplateResponse
from django.template import RequestContext

def Kategoriler(request, slug):
    kategori=Kategori.objects.all()
    kategorim=get_object_or_404(Kategori, slug=slug)
    makale=Makale.objects.filter(kategori=kategorim)
    
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    ctx={'sosyal':sosyal,'kategorim':kategorim,'makale':makale,'ayar':ayar}
    return TemplateResponse(request,"kategoriBlog.html",ctx)
    #return render_to_response("kategoriBlog.html",locals())

#def Etiket(TaggedItemBase):
 #   gonderiler=Makale.objects.filter(tags_name=etiketler)
  #  return render_to_response("etiketler.html", {'gonderiler':gonderiler ,'etiketler':etiketler})

def BlogAnasayfa(request):
    makale=Makale.objects.all()
    sosyal=SosyalMedya.objects.all()
    ayar=Ayarlar.objects.all()
    kategori=Kategori.objects.all()

    icerikteAra=""
    aranacak_kelime=""
    arama_formu=AramaFormu(request.GET)
    if request.GET.get('aranacak_kelime'):
        arama_formu=AramaFormu(request.GET)
        if arama_formu.is_valid():
            aranacak_kelime=arama_formu.cleaned_data['aranacak_kelime']
            icerikteAra=Makale.objects.filter(icerik__contains=aranacak_kelime)

            return render_to_response("search.html", {'icerikteAra':icerikteAra})

    sayfalama=Paginator(makale, 3)
    sayfaNo=request.GET.get('sayfa')  
    try:
        sayfa=sayfalama.page(sayfaNo)
    except PageNotAnInteger:
        sayfa=sayfalama.page(1)
    except EmptyPage:
        sayfa=sayfalama.page(sayfalama.num_pages)

    ctx={'makale':makale,'ayar':ayar,'sosyal':sosyal,'kategori':kategori,'sayfa':sayfa,'arama_formu':arama_formu,'icerikteAra':icerikteAra,'aranacak_kelime':aranacak_kelime}
    #return TemplateResponse(request, "blog.html",ctx)
    return render_to_response("blog.html", ctx,context_instance=RequestContext(request))

def BlogDetay(request, slug):
    #detay=Makale.objects.all()
    kategori=Kategori.objects.all()
    detay=get_object_or_404(Makale, slug=slug)
    ayar=Ayarlar.objects.all()
    sosyal=SosyalMedya.objects.all()
    arama_formu=AramaFormu(request.GET)
    icerikteAra=""
    aranacak_kelime=""
    if request.GET.get('aranacak_kelime'):
        arama_formu=AramaFormu(request.GET)
        if arama_formu.is_valid():
            aranacak_kelime=arama_formu.cleaned_data['aranacak_kelime']
            icerikteAra=Makale.objects.filter(icerik__contains=aranacak_kelime)
            return render_to_response("search.html", {'icerikteAra':icerikteAra})
    ctx={'kategori':kategori,'detay':detay,'sosyal':sosyal,'ayar':ayar,'arama_formu':arama_formu,'icerikteAra':icerikteAra,'aranacak_kelime':aranacak_kelime}
    #return render_to_response("detay.html",locals(),{'blog':blog})
    return TemplateResponse(request,"detay.html",ctx)
