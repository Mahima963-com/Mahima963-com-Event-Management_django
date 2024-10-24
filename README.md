

# Event Management System

This Django project is an Event Management System that allows users to manage events, attendees, and tickets. It includes features like CSV file upload to create events, attendee registration, ticket tracking, and reporting of ticket sales and revenue.

## Features

- **Event Management:**
  - Create, update, and delete events.
  - Track event details like title, description, date, location, capacity, ticket price, and tickets sold.
  
- **Attendee Management:**
  - Register attendees for events.
  - View and update attendee details.
  - List of attendees for each event.

- **Ticket Management:**
  - Track tickets sold and remaining based on event capacity.
  - Calculate total revenue generated from ticket sales.

- **CSV Upload:**
  - Upload CSV files to create new events in bulk.
  - CSV format: `title, description, date, location, capacity, Cost`.

## Getting Started

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- Django
- SQLite (default Django database)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mahima963-com/Event-Management_django
   cd event-management-system
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the admin panel**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open a web browser and navigate to `http://127.0.0.1:8000/`.

### CSV Upload Format

To upload events using a CSV file, ensure that the CSV file follows the format:

```csv
title,description,date,location,capacity,ticket_price
Event 1,Description for Event 1,2024-10-31 14:00:00,New York,100,50.00
Event 2,Description for Event 2,2024-11-05 10:00:00,London,150,60.00
```

### File Structure

```bash
event-management-system/
│
├── events/               # Django app for managing events
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates for the project
│   ├── forms.py          # Django forms for event and CSV upload
│   ├── models.py         # Database models for events, attendees, and tickets
│   ├── views.py          # Views for handling business logic
│   └── urls.py           # URL routing for the app
│
├── project_name/         # Main project directory
│   └── settings.py       # Project settings
│
├── manage.py             # Django's management utility
└── README.md             # Project documentation (this file)
```

## Usage

### Event Management

- **List Events**: View a list of all events.
- **Create Event**: Create a new event by filling out the event form or by uploading a CSV file.
- **Edit Event**: Update the details of an existing event.
- **Delete Event**: Remove an event from the system.

### Attendee Management

- **Register Attendees**: Register new attendees for an event.
- **Update Attendee**: Update the information of an attendee.
- **View Attendees**: See a list of all attendees for a specific event.

### Ticket Sales and Revenue

- **Track Tickets**: Track how many tickets have been sold and how many are remaining for each event.
- **Revenue Calculation**: See the total revenue generated for each event based on ticket sales.



