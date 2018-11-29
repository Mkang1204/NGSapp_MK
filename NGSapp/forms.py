from django import forms
from NGSapp.models import Run


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            # 'class': 'form-control',
            
        }
    ))