from rest_framework.permissions import BasePermission

class IsPatientOwner(BasePermission):
def has_object_permission(self, request, view, obj):
return obj.user_id == request.user.id

class IsDoctorOwner(BasePermission):
def has_object_permission(self, request, view, obj):
return obj.user_id == request.user.id

class IsMappingOwner(BasePermission):
def has_object_permission(self, request, view, obj):
return (
obj.patient.user_id == request.user.id
and obj.doctor.user_id == request.user.id
)
