from django import forms

from app.models import Place,Top_list


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


class ToplistForm(forms.ModelForm):
    class Meta:
        model = Top_list
        fields = '__all__'