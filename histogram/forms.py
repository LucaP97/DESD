from django import forms
from histogram.models import logMessage

class logMessageForm(forms.ModelForm):
    class Meta:
        model = logMessage
        fields = ("message",) # NOTE, the trailing comma is required