from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
list_display = ("id", "name", "age", "gender", "user")
search_fields = ("name", "phone")
list_filter = ("gender",)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
list_display = ("id", "name", "specialization", "email", "user")
search_fields = ("name", "email", "specialization")

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
list_display = ("id", "patient", "doctor", "assigned_at")
