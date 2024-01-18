from django.contrib import admin
from .models import UserProfile , Hospital , AmbulanceDriver , Patient
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Hospital)
admin.site.register(AmbulanceDriver)
admin.site.register(Patient)