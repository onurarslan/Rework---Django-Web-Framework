from django import forms

class iletisimFormu(forms.Form):
    isim=forms.CharField()
    email=forms.EmailField()
    mesaj=forms.CharField(widget=forms.Textarea)

