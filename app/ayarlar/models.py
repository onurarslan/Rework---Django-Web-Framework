from django.db import models

class SosyalMedya(models.Model):
    twitterWidget=models.TextField(blank=True)
    twitterURL=models.URLField(blank=True)
    facebookURL=models.URLField(blank=True)
    linkedinURL=models.URLField(blank=True)
    class Meta:
        verbose_name_plural="Sosyal Medya"

class Ayarlar(models.Model):
    siteBaslik=models.CharField(max_length=70,blank=True)
    slugBaslik=models.SlugField(max_length=70,blank=True)
    sakliHaklar=models.CharField(max_length=75,blank=True)
    siteAciklama=models.CharField(max_length=160,blank=True)
    anahtarKelimeler=models.CharField(max_length=260,blank=True)
    siteAdresi=models.URLField()
    siteSlogan=models.CharField(max_length=30,blank=True)
    siteLogo=models.ImageField(upload_to="images/",blank=True)
    iletisimMail=models.EmailField(blank=True)
    iletisimAdres=models.TextField(blank=True)
    iletisimTel1=models.IntegerField(max_length=11,blank=True)
    iletisimTel2=models.IntegerField(max_length=11,blank=True)
    googleAnalytics=models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural="Ayarlar"

class Manset(models.Model):
    mansetResim=models.ImageField(upload_to="images/")
    mansetBaslik=models.CharField(max_length=70)
    slug=models.SlugField(max_length=70)
    mansetOzet=models.CharField(max_length=160)
    mansetMetin=models.TextField()

    class Meta:
        verbose_name_plural="Manşet"

    def __unicode__(self):
        return self.mansetBaslik
    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return '%s' %(self.slug)
    ordering= ['-id']

class Referanslar(models.Model):
    referansLogo=models.ImageField(upload_to="images/")
    referansLink=models.URLField(blank=True)
    class Meta:
        verbose_name_plural="Referanslar"
