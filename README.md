# Hospital Appointment Management System

A Django-based web application for managing hospital departments, doctors, patients, appointment hours, and patient appointments.
The system includes dynamic doctor filtering based on department selection and displays available/unavailable hours using AJAX.

## Project Structure
hospitalprj/
 ├── hospitalapp/
 │   ├── migrations/
 │   ├── static/
 │   │   └── css/
 │   │       └── navbar.css
 │   ├── templates/
 │   │   ├── home.html
 │   │   ├── add_department.html
 │   │   ├── add_doctor.html
 │   │   ├── add_patient.html
 │   │   ├── add_time.html
 │   │   ├── add_appointment.html
 │   │   ├── list_department.html
 │   │   ├── list_doctor.html
 │   │   ├── list_patient.html
 │   │   ├── list_time.html
 │   │   └── list_appointment.html
 │   ├── models.py
 │   ├── views.py
 │   ├── urls.py
 │   └── admin.py
 ├── hospitalprj/
 │   ├── settings.py
 │   ├── urls.py
 │   └── wsgi.py
 ├── manage.py
 └── README.md

## Features
### Department Management

Add new departments

List all departments

### Doctor Management

Add doctors and assign a department

List all doctors

AJAX-based doctor filtering by department

### Patient Management

Add new patients

List all patients

### Time Management

Add available time slots

List time slots

### Appointment Management

Add new appointments

Automatically checks unavailable hours

Dynamic doctor filtering based on department

Marks booked appointment hours as unavailable

## Database Models Overview
### Departments
departmentname = CharField(max_length=100)

### Doctors
doctornamesurname = CharField(max_length=100)
department = ForeignKey(Departments, on_delete=models.CASCADE)

### Patients
patientname = CharField(max_length=100)
patientsurname = CharField(max_length=100)
patienttcno = CharField(max_length=11)

### Times
hour = TimeField()

### Appointments
appointmentdate = DateField()
patient = ForeignKey(Patients)
doctor = ForeignKey(Doctors)
time = ForeignKey(Times)


## AJAX Features
1. Fetch doctors based on selected department

Triggered when the user changes the department in Appointment form.

$.ajax({
    url: "{% url 'get_doctors_by_department' %}",
    data: { 'department_id': departmentId },
    success: function(doctors) {
        // Populates doctor dropdown
    }
});

2. Fetch available/unavailable hours

Triggered when user selects a doctor or date.

$.ajax({
    url: "{% url 'get_available_hours' %}",
    data: { 'doctor_id': doctorId, 'appointment_date': date },
    success: function(data) {
        // Marks times as booked/unavailable
    }
});

##  How the Appointment Form Works

User enters patient details

User selects a department

AJAX loads doctors in that department

User selects a date

AJAX loads available time slots

Booked times are disabled

Appointment is saved


## Front-End (Static Files)
Navbar (navbar.css)

Used across all templates.

.navbar{
    display: flex;
    justify-content: space-between;
    background-color: aquamarine;
}

## Installation
1. Clone project
git clone <repository-url>
cd hospitalprj

2. Install dependencies
pip install django

3. Run migrations
python manage.py migrate

4. Start server
python manage.py runserver

5. Open in browser
http://127.0.0.1:8000/

## License
This project currently has no license.
You may add one if you plan to publish or distribute it publicly.
