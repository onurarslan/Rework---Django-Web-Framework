from app.iletisim.forms import iletisimFormu
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, mail_admins
from django.shortcuts import render_to_response
from app.ayarlar.models import *

def iletisimeGec(request):
    basariDurumu=False
    isim=""
    email=""
    mesaj=""
    ayar=Ayarlar.objects.all()
    sosyal=SosyalMedya.objects.all()

    if request.method=="POST":
        iletisim=iletisimFormu(request.POST)

        if iletisim.is_valid():
            basariDurumu=True
            isim=iletisim.cleaned_data['isim']
            email=iletisim.cleaned_data['email']
            mesaj=iletisim.cleaned_data['mesaj']
            alici=['user.to@server.com']


            send_mail("Yeni Mesaj", "\nGönderen: %s\nE-Posta: %s \nMesaj: %s" %(isim,email,mesaj),'a.a.com', ['a@a.com'],  fail_silently=True)
            mail_admins("Yeni Mesaj", "\nGönderen: %s\nE-Posta: %s\nMesaj: %s" %(isim,email,mesaj) , fail_silently=True)

    else:
        iletisim=iletisimFormu()
    ctx={'iletisim': iletisim, 'isim':isim,'sosyal':sosyal, 'email':email,'mesaj':mesaj, 'basariDurumu':basariDurumu,'ayar':ayar}
    return render_to_response("iletisim.html", ctx, context_instance=RequestContext(request))
