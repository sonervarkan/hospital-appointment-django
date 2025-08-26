from django.db import models

# Create your models here.

class Departments(models.Model):
    departmentname=models.CharField(max_length=100)

    def __str__(self):
        return self.departmentname

class Doctors(models.Model):
    doctornamesurname=models.CharField(max_length=100)
    department=models.ForeignKey(Departments, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.doctorname}-{self.department}"

class Patients(models.Model):
    patientname=models.CharField(max_length=100)
    patientsurname=models.CharField(max_length=100)
    patienttcno=models.CharField(max_length=11)


    def __str__(self):
        return f"{self.patientname}-{self.patientsurname}-{self.patienttcno}"

class Times(models.Model):
    hour=models.TimeField()

    def __str__(self):
        return f"{self.hour}"
    
class Appointments(models.Model):
    appointmentdate=models.DateField()
    patient=models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    time=models.ForeignKey(Times, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointmentdate}-{self.patient}-{self.doctor}-{self.time}"
    

