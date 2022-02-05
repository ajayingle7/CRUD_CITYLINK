from django import forms
from .models import City,Zip


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

        labels = {'cid':'City Id','cname':'City Name','dist':'District','state':'State'}

        widgets = {'cid':forms.NumberInput(attrs={'class':'form-control'}),
                   'cname':forms.TextInput(attrs={'class':'form-control'}),
                   'dist':forms.TextInput(attrs={'class':'form-control'}),
                   'state':forms.TextInput(attrs={'class':'form-control'})}



class ZipForm(forms.ModelForm):
    class Meta:
        model = Zip
        fields = '__all__'

        labels = {'area':'AREA','zip':'ZIP'}

        widgets = {'area':forms.TextInput(attrs={'class':'form-control'}),
                   'zip':forms.TextInput(attrs={'class':'form-control'})}


