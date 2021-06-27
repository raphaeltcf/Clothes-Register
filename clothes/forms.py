from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = "__all__"
