from django.conf import settings
from django.db import models

class Patient(models.Model):
user = models.ForeignKey(
settings.AUTH_USER_MODEL,
on_delete=models.CASCADE,
related_name="patients",
)
name = models.CharField(max_length=150)
age = models.PositiveIntegerField()
gender = models.CharField(max_length=20)
address = models.TextField()
phone = models.CharField(max_length=20)
created_at = models.DateTimeField(auto_now_add=True)

```
def __str__(self):
    return self.name
```

class Doctor(models.Model):
user = models.ForeignKey(
settings.AUTH_USER_MODEL,
on_delete=models.CASCADE,
related_name="doctors",
)
name = models.CharField(max_length=150)
specialization = models.CharField(max_length=150)
phone = models.CharField(max_length=20)
email = models.EmailField(unique=True)
created_at = models.DateTimeField(auto_now_add=True)

```
def __str__(self):
    return self.name
```

class PatientDoctorMapping(models.Model):
patient = models.ForeignKey(
Patient,
on_delete=models.CASCADE,
related_name="doctor_mappings",
)
doctor = models.ForeignKey(
Doctor,
on_delete=models.CASCADE,
related_name="patient_mappings",
)
assigned_at = models.DateTimeField(auto_now_add=True)

```
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["patient", "doctor"],
            name="unique_patient_doctor_mapping",
        )
    ]

def __str__(self):
    return f"{self.patient.name} - {self.doctor.name}"
```
