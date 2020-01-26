from django import forms

class SendMessageForm(forms.Form):
    number = forms.CharField(label='Number', max_length=10000)
    text = forms.CharField(label='Text', max_length=300)
