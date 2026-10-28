from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
RegisterView,
LoginView,
PatientViewSet,
DoctorViewSet,
PatientDoctorMappingViewSet,
)

router = DefaultRouter()
router.register("patients", PatientViewSet, basename="patient")
router.register("doctors", DoctorViewSet, basename="doctor")
router.register("mappings", PatientDoctorMappingViewSet, basename="mapping")

urlpatterns = [
path("auth/register/", RegisterView.as_view(), name="register"),
path("auth/login/", LoginView.as_view(), name="login"),
path("", include(router.urls)),
]
