from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class Kategori(models.Model):
    baslik=models.CharField(max_length=50)
    slug=models.SlugField(max_length=75)

    def __unicode__(self):
        return self.baslik

    def __unicode__(self):
        return self.slug
    
    class Meta:
        verbose_name_plural="Kategoriler"

    def get_absolute_url(self):
        return '%s' %(self.slug)

#class Etiket(TaggedItemBase):
#    etiket=models.ForeignKey('Makale') 

#class Yazar(models.Model):
#    isim=models.CharField(max_length=50)
#    slug=models.SlugField(max_length=20)

#    class Meta:
#        verbose_name_plural="Yazarlar"
#
 #   def __unicode__(self):
  #      return self.isim

class Makale(models.Model):
    kategori=models.ForeignKey('Kategori')
    baslik=models.CharField(max_length=50)
   # yazar=models.ForeignKey('Yazar')
    sayac=models.IntegerField(default=0)
    resim=models.ImageField(upload_to="media/images/")
    icerik=models.TextField()
    icerikOzet=models.CharField(max_length=190)
    slug=models.SlugField(max_length=60)
    yayin_tarihi=models.DateField(auto_now_add=True)
    #etiketler=TaggableManager()
    #models.ForeignKey('Etiket')
    class Meta:
        verbose_name_plural="Makale Ekle"
        ordering =['-id']
    
    def __unicode__(self):
        return self.slug

    def __unicode__(self):
        return self.baslik
     
    def get_absolute_url(self):
        return '%s' %(self.slug)
