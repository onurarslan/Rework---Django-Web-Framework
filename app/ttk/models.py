from django.db import models

class TicaretSicilBilgileri(models.Model):
    unvan=models.CharField(max_length=255)
    kurulusTarihi=models.DateField()
    sirketMerkezi=models.CharField(max_length=255)
    adres=models.CharField(max_length=255)
    kayitliOlduguSicil=models.CharField(max_length=255)
    ticaretSicilNo=models.CharField(max_length=255)
    tescilTarihi=models.DateField()
    odenmisSermaye=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Ticaret Sicil Bilgileri"
        
class OrtaklikYapisi(models.Model):
    ortak=models.CharField(max_length=255)
    ortakCiro=models.CharField(max_length=255)
    ortakYuzde=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Ortaklık Yapısı"

class YonetimKurulu(models.Model):
    gorevi=models.CharField(max_length=255)
    adiSoyadi=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Yönetim Kurulu"
class Denetciler(models.Model):
    adiSoyadi=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Denetçiler"

class UstYonetim(models.Model):
    gorevi=models.CharField(max_length=255)
    adiSoyadi=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Üst Yönetim"

class DonemselFinansalSonuclar(models.Model):
    finansalYili=models.CharField(max_length=4)
    finansalUcAylik=models.FileField(upload_to="finans", blank=True)
    finansalAltiAylik=models.FileField(upload_to="finans", blank=True)
    finansalDokuzAylik=models.FileField(upload_to="finans", blank=True)
    finansalOnIkiAylik=models.FileField(upload_to="finans", blank=True)
    class Meta:
        verbose_name_plural="Dönemsel Finansal Sonuçları"
        ordering=['-id']

class FaaliyetRaporlari(models.Model):
    faaliyetYili=models.CharField(max_length=4)
    faaliyetBirinciCeyrek=models.FileField(upload_to="faaliyet", blank=True)
    faaliyetIkinciCeyrek=models.FileField(upload_to="faaliyet", blank=True)
    faaliyetUcuncuCeyrek=models.FileField(upload_to="faaliyet", blank=True)
    faaliyetYillikRapor=models.FileField(upload_to="faaliyet", blank=True)
    class Meta:
        verbose_name_plural="Faaliyet Raporları"
        ordering=['-id']

class GenelKurulBilgileri(models.Model):
    aciklama=models.CharField(max_length=255)
    dosya=models.FileField(upload_to="kurul", blank=True)
