
from marks.models import Mark
from django import forms
from django.forms import ModelForm
class UpdateMarksForm(ModelForm):
    class Meta:
        model = Mark
        fields = ['ca']