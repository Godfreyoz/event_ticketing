# tickets/forms.py
from django import forms
from .models import Event, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event']
