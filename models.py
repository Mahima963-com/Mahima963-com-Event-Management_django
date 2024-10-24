from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Ticket price
    tickets_sold = models.IntegerField(default=0)  # Tracks how many tickets are sold

    def __str__(self):
        return self.title

    # Method to calculate the number of remaining tickets
    def remaining_tickets(self):
        return max(self.capacity - self.tickets_sold, 0)

    # Method to calculate total revenue generated from tickets
    def total_revenue(self):
        return self.tickets_sold * self.ticket_price

class Attendee(models.Model):
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.event.title}'

    # Method to count attendees for an event
    @staticmethod
    def count_attendees(event_id):
        return Attendee.objects.filter(event_id=event_id).count()

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event.title} - Ticket {self.id}"

    # Additional method to track ticket sales for an event
    @staticmethod
    def count_sold_tickets(event_id):
        return Ticket.objects.filter(event_id=event_id, sold=True).count()



