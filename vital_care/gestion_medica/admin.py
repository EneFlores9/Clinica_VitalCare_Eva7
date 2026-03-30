from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Doctor, HoraMedica

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(HoraMedica)