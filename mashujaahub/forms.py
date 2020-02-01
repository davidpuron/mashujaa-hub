from django import forms
from registration import models

class SendMessageForm(forms.Form):
    group = forms.ChoiceField( choices=models.TYPE_CHOICES, initial='NO')
    number = forms.CharField(label='Numbers', max_length=10000, widget=forms.Textarea, initial='None')
    text = forms.CharField(label='Text', max_length=300, widget=forms.Textarea)
