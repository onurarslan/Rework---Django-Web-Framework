from django.db import models

class Hakkimizda(models.Model):
    hakkimizda=models.TextField(blank=True)
    misyonumuz=models.TextField(blank=True)
    vizyonumuz=models.TextField(blank=True)
    class Meta:
        verbose_name_plural="Hakkımızda"
    
class Yoneticilerimiz(models.Model):
    yoneticiResmi=models.ImageField(upload_to="images/")
    yoneticiAdiSoyadi=models.CharField(max_length=60)
    yoneticiPozisyonu=models.CharField(max_length=60)
    yoneticiHakkinda=models.CharField(max_length=25)
    yoneticiTwitter=models.URLField(blank=True)
    yoneticiLinkedin=models.URLField(blank=True)
    yoneticiFacebook=models.URLField(blank=True)
    class Meta:
        verbose_name_plural="Yöneticilerimiz"
