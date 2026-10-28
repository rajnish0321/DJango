from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
name = serializers.CharField(source="first_name", max_length=150)
password = serializers.CharField(
write_only=True,
min_length=8,
trim_whitespace=False,
)

```
class Meta:
    model = User
    fields = ["id", "name", "email", "password"]

def validate_email(self, value):
    value = value.strip().lower()

    if User.objects.filter(email__iexact=value).exists():
        raise serializers.ValidationError(
            "A user with this email already exists."
        )

    return value

def create(self, validated_data):
    password = validated_data.pop("password")
    validated_data["username"] = validated_data["email"]

    return User.objects.create_user(
        password=password,
        **validated_data,
    )
```

class PatientSerializer(serializers.ModelSerializer):
class Meta:
model = Patient
fields = [
"id", "name", "age", "gender",
"address", "phone", "created_at",
]
read_only_fields = ["id", "created_at"]

```
def validate_age(self, value):
    if value > 120:
        raise serializers.ValidationError(
            "Age must not exceed 120."
        )
    return value
```

class DoctorSerializer(serializers.ModelSerializer):
class Meta:
model = Doctor
fields = [
"id", "name", "specialization",
"phone", "email", "created_at",
]
read_only_fields = ["id", "created_at"]

```
def validate_email(self, value):
    value = value.strip().lower()

    queryset = Doctor.objects.filter(email__iexact=value)

    if self.instance:
        queryset = queryset.exclude(pk=self.instance.pk)

    if queryset.exists():
        raise serializers.ValidationError(
            "A doctor with this email already exists."
        )

    return value
```

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
patient_name = serializers.CharField(
source="patient.name",
read_only=True,
)
doctor_name = serializers.CharField(
source="doctor.name",
read_only=True,
)

```
class Meta:
    model = PatientDoctorMapping
    fields = [
        "id", "patient", "patient_name",
        "doctor", "doctor_name", "assigned_at",
    ]
    read_only_fields = ["id", "assigned_at"]
```
