from django import forms
from histogram.models import logMessage

class logMessageForm(forms.ModelForm):
    class Meta:
        model = logMessage
        fields = ("message", "logger") # NOTE, the trailing comma is required