from django import forms
from .models import Conference

class conferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ('name', 'venue', 'city', 'state', 'details')