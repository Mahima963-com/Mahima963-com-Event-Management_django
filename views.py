from django.shortcuts import render

# views.py
import csv
from django.contrib import messages
from .forms import CSVUploadForm

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django import forms
import csv
from django.http import HttpResponse

from .models import Event, Attendee
from .forms import AttendeeForm

'''def event_attendees(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendees = event.attendees.all()  # Assuming `Attendee` model has a ForeignKey to `Event`
    return render(request, 'events/event_attendees.html', {'event': event, 'attendees': attendees})'''
from django.shortcuts import render, get_object_or_404
from .models import Event, Attendee, Ticket

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    
    remaining_tickets = event.capacity - Attendee.count_attendees(id)  # Remaining tickets
    total_revenue = event.ticket_price * Attendee.count_attendees(id)  # Total revenue from ticket sales
    attendees_count = Attendee.count_attendees(id)  # Total attendees
    tickets_sold = Attendee.count_attendees(id)   # Total tickets sold

    return render(request, 'events/event_detail.html', {
        'event': event,
        'remaining_tickets': remaining_tickets,
        'total_revenue': total_revenue,
        'attendees_count': attendees_count,
        'tickets_sold': tickets_sold
    })
# Register Attendee
def register_attendee(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_attendees.html')
    else:
        form = AttendeeForm()
    return render(request, 'events/attendee_form.html', {'form': form})

# Update Attendee
def update_attendee(request, id):
    attendee = get_object_or_404(Attendee, id=id)
    if request.method == 'POST':
        form = AttendeeForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            return redirect('event_attendees')  # Redirect to the attendee list or the event attendee view
    else:
        form = AttendeeForm(instance=attendee)
    return render(request, 'events/attendee_form.html', {'form': form})

# View Attendees for a Specific Event
# views.py
from django.shortcuts import render
from .models import Event

def event_attendees(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'events/event_attendees.html', {'events': events})



class CSVImportForm(forms.Form):
    csv_file = forms.FileField()


def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            Event.objects.create(
                title=row['Event Title'],
                description=row['Description'],
                date=row['Date'],
                location=row['Location'],
                capacity=row['Capacity']
            )
        return redirect('event_list')

    return render(request, 'events/import_csv.html', {'form': CSVImportForm()})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})




def csv_upload(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            # Check if the file is a CSV
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file.')
                return redirect('csv_upload')

            # Parse the CSV file
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)

                # Iterate through rows and create Event instances
                for row in reader:
                    # Ensure that CSV fields match the Event model fields
                    Event.objects.create(
                        title=row['title'],
                        description=row['description'],
                        date=row['date'],  # Date format in CSV must match Django's DateTimeField
                        location=row['location'],
                        capacity=row['capacity'],
                    )
                messages.success(request, 'CSV file uploaded successfully!')
                return redirect('event_list')
            except Exception as e:
                messages.error(request, f'Error processing the CSV file: {e}')
                return redirect('csv_upload')
    else:
        form = CSVUploadForm()
    return render(request, 'events/csv_upload.html', {'form': form})

