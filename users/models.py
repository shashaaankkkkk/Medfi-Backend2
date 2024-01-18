# users/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('hospital', 'Hospital'),
        ('ambulance_driver', 'Ambulance Driver'),
        ('patient', 'Patient'),
        # Add other roles as needed
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    # Add other custom fields based on roles

    # Override the groups and user_permissions fields with related_name='+'
    groups = models.ManyToManyField(Group, blank=True, related_name='+')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='+')

# Example of adding a custom field for a hospital
class Hospital(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='hospital_profile')
    hospital_name = models.CharField(max_length=255)
    # Add other hospital-specific fields

# Example of adding a custom field for an ambulance driver
class AmbulanceDriver(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=20)
    # Add other ambulance driver-specific fields

# Example of adding a custom field for a patient
class Patient(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='patient_profile')
    medical_history = models.TextField()
    # Add other patient-specific fields
