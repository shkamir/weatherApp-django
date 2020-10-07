from django import forms
from .models import City 

class CityForm(forms.Form):
    name = forms.CharField(label="",
    max_length=25,
    )
    def clean_name(self):
        name = self.cleaned_data.get('name')
        r = City.objects.filter(name=name)
        if name.count:
            raise forms.ValidationError("{0} already exists".format(name))
        return name