from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^blog/$', 'app.blog.views.BlogAnasayfa', name='BlogAnasayfa'),
    url(r'^blog/(?P<slug>[-\w]+)/$','app.blog.views.BlogDetay', name='BlogDetay'),
    #url(r'^blog/$',include('blog.urls')),
    url(r'^$', 'app.ayarlar.views.Index', name='anasayfa'),
    url(r'^index.html', 'app.ayarlar.views.Index'),
    url(r'^iletisim.html', 'app.iletisim.views.iletisimeGec', name='iletisim'),
    #url(r'^a.html','app.blog.views.BlogAnasayfa'),
    url(r'^hakkimizda/', include('django.contrib.flatpages.urls')),
    #url(r'^etiketler/(?P<tag>\w+)$', 'tagpage'),
    url(r'^base.html/','app.ayarlar.views.ayarSite'),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^/(?P<slug>[-\w]+)/$', 'app.ayarlar.views.Index'),
    url(r'^manset/(?P<slug>[-\w]+)/$','app.ayarlar.views.MansetAc', name='MansetAc'),
    url(r'^portfolio/$','app.portfolio.views.PortfolioGiris',name='PortfolioGiris'),
    url(r'^portfolio/(?P<slug>[-\w]+)/$', 'app.portfolio.views.PortfolioDetay', name='PortfolioDetay'),
    url(r'^hakkimizda.html$','app.hakkimizda.views.HakkimizdaView', name='HakkimizdaView'),
    url(r'^kategori/(?P<slug>[-\w]+)/$','app.blog.views.Kategoriler'),
    url(r'^portfolio/kategori/(?P<slug>[-\w]+)/$','app.portfolio.views.Kategoriler'),
    url(r'^ttk.html$','app.ttk.views.ticaretSicilBilgileri', name='ttk'),
    url(r'^ortaklikYapisi.html$','app.ttk.views.ortaklikYapisi',name='oy'),
    url(r'^yonetimKurulu.html$','app.ttk.views.yonetimKurulu',name='yk'),
    url(r'^denetciler.html$','app.ttk.views.denetciler',name='denetci'),
    url(r'^ustYonetim.html$','app.ttk.views.ustYonetim',name='uy'),
    url(r'^donemselFinans.html$','app.ttk.views.donemselFinans',name='df'),
    url(r'^faaliyetRaporlari.html$','app.ttk.views.faaliyetRaporlari', name='fr'),
    url(r'^genelKurul.html$','app.ttk.views.genelKurulBilgileri', name='gk'),
    #url(r'^index.html','ayarlar.views.Anasayfa'),
                       
    # url(r'^rework/', include('rework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns( )

urlpatterns+=patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$','flatpage')
                      )
