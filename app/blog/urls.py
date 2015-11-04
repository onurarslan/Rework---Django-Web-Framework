from django.conf.urls import patterns, include, url

urlpatterns=patterns('blog.views',
    url(r'^', 'BlogAnasayfa', name='BlogAnasayfa'),
    url(r'^(?P<slug>[-\w]+)/$','BlogDetay', name='BlogDetay'),
                     )
