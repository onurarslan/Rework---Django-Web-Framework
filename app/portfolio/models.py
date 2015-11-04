from django.db import models

class Kategori(models.Model):
    baslik=models.CharField(max_length=60)
    slug=models.SlugField(max_length=60)

    class Meta:
        verbose_name_plural="Kategoriler"

    def __unicode__(self):
        return self.slug
        
    def __unicode__(self):
        return self.baslik

    def get_absolute_url(self):
        return '/portfolio/kategori/%s' %(self.slug)

class Portfolio(models.Model):
    portfolioResim=models.ImageField(upload_to="images/")
    #kucukResim
    portfolioBaslik=models.CharField(max_length=60)
    kategori=models.ForeignKey('Kategori')
    slug = models.SlugField(max_length=60)
    #genelGorunum=models.TextField()
    #portfolioResim1=models.ImageField(upload_to="images/")
    #portfolioResim2=models.ImageField(upload_to="images/")
    #portfolioResim3=models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural="Portfolio"

    def __unicode__(self):
        return self.slug

    def __unicode__(self):
        return self.portfolioBaslik

    def get_absolute_url(self):
        return '%s' %(self.slug)
