from django import forms
from django.forms import ModelForm
from .models import News

# Create a new form
# Video used to create this part
# https://www.youtube.com/watch?v=CVEKe39VFu8&t=1303s&ab_channel=Codemy.com
class NewForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'description', 'new_img_url', 'country')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'new_img_url': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
        }