from django import forms
from . import models


class UpdateForms(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content')
