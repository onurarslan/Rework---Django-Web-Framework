from django import forms
class AramaFormu(forms.Form):
    aranacak_kelime=forms.CharField()

    def clean_aranacak_kelime(self):
        kelime=self.cleaned_data['aranacak_kelime']
        if len(kelime)<3:
            raise forms.ValidationError('Aranacak kelime 3 harften az olamaz.')
        return kelime
