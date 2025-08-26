from django.shortcuts import render, redirect
from .models import Departments, Doctors, Patients, Times, Appointments
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def list_department(request):
    departments=Departments.objects.all()
    return render(request,'list_department.html', {'departments':departments})

def add_department(request):
    if request.method=='POST':
        departmentname=request.POST.get('departmentname')

        new_department=Departments(departmentname=departmentname)
        new_department.save()
        return redirect('list_department')

    return render(request,'add_department.html')

def list_doctor(request):
    doctors=Doctors.objects.all()

    return render(request,'list_doctor.html', {'doctors':doctors})

from django.shortcuts import render, redirect
from .models import Doctors, Departments

def add_doctor(request):
    if request.method == 'POST':
        doctornamesurname = request.POST.get('doctornamesurname')
        department_id = request.POST.get('department_id')

        
        department_obj = Departments.objects.get(id=department_id)

       
        new_doctor = Doctors(doctornamesurname=doctornamesurname, department=department_obj)
        new_doctor.save()

        return redirect('list_doctor')


    departments = Departments.objects.all()
    return render(request, 'add_doctor.html', {'departments': departments})

def list_patient(request):
    patients=Patients.objects.all()
    return render(request,'list_patient.html', {'patients':patients})

def add_patient(request):
    if request.method=="POST":
        patientname=request.POST.get('patientname')
        patientsurname=request.POST.get('patientsurname')
        patienttcno=request.POST.get('patienttcno')

        new_patient=Patients(patientname=patientname, patientsurname=patientsurname, patienttcno=patienttcno)
        new_patient.save()
        return redirect('list_patient')

    return render(request,'add_patient.html')

def list_time(request):
    times=Times.objects.all()
    return render(request,'list_time.html', {'times':times})

def add_time(request):
    if request.method=="POST":
        hour=request.POST.get('hour')

        new_time=Times(hour=hour)
        new_time.save()
        return redirect('list_time')

    return render(request,'add_time.html')


def list_appointment(request):
    appointments=Appointments.objects.all()
    return render(request,"list_appointment.html",{"appointments":appointments})

def add_appointment(request):
    if request.method=="POST":
          
        patientname=request.POST.get("patientname")
        patientsurname=request.POST.get("patientsurname")
        patienttcno=request.POST.get("patienttcno")
        new_patient=Patients(patientname=patientname, patientsurname=patientsurname, patienttcno=patienttcno)
        new_patient.save()

        appointmentdate=request.POST.get("appointmentdate")

        department_id=request.POST.get("department_id")
        doctor_id=request.POST.get("doctor_id")
        time_id=request.POST.get("time_id")

        department_obj=Departments.objects.get(id=department_id)
        doctor_obj=Doctors.objects.get(id=doctor_id)
        time_obj=Times.objects.get(id=time_id)

        new_appointment = Appointments(
            appointmentdate=appointmentdate, 
            patient=new_patient, 
            doctor=doctor_obj, 
            time=time_obj
        )
        new_appointment.save()
        return redirect("list_appointment")

    # POST değil de GET ise
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()
    times = Times.objects.all()
    
    context = {
        'departments': departments,
        'doctors': doctors,
        'times': times,
    }
    return render(request, "add_appointment.html", context)

# Seçilen departmentname'e bağlı doctornamesurname listelemesi
def get_doctors_by_department(request):
    department_id = request.GET.get('department_id')
    doctors = Doctors.objects.filter(department_id=department_id).values('id', 'doctornamesurname')
    return JsonResponse(list(doctors), safe=False)

def get_available_hours(request):
    doctor_id = request.GET.get('doctor_id')
    appointment_date = request.GET.get('appointment_date')
    
    if not doctor_id or not appointment_date:
        return JsonResponse({'error': 'Doctor ID and appointment date are required.'}, status=400)

    booked_time_ids = Appointments.objects.filter(
        doctor_id=doctor_id,
        appointmentdate=appointment_date
    ).values_list('time_id', flat=True)

    all_times = Times.objects.all().values('id', 'hour')
    
    response_data = []
    for time in all_times:
        is_booked = time['id'] in booked_time_ids
        response_data.append({
            'id': time['id'],
            'hour': time['hour'],
            'is_booked': is_booked
        })
        
    return JsonResponse(response_data, safe=False)