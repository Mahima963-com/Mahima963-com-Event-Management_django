from django.contrib import admin

# Register your models here.

from .models import Event,Attendee,Ticket

admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Ticket)