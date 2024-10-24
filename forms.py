from django import forms
from .models import Event
from .models import Attendee
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'capacity', 'ticket_price']  # Added 'ticket_price'


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'phone', 'event']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Select CSV File", help_text="Upload a CSV file with event data.")
