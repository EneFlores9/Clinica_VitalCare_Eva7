from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Paciente, Doctor

class ClinicaTest(TestCase):
    def setUp(self):
        # Creamos datos de prueba iniciales
        self.doctor = Doctor.objects.create(
            nombre="Camilo", 
            apellido="Rojas", 
            edad=40, 
            fecha_nacimiento="1984-05-10", 
            especialidad="Pediatría"
        )
        self.paciente = Paciente.objects.create(
            nombre="Lucas", 
            apellido="Soto", 
            edad=10, 
            fecha_nacimiento="2014-03-15"
        )

    # 3 Validaciones para el modelo Doctor
    def test_doctor_validaciones(self):
        doc = Doctor.objects.get(apellido="Rojas")
        self.assertEqual(doc.nombre, "Camilo")         # Validación 1: Nombre correcto
        self.assertEqual(doc.especialidad, "Pediatría") # Validación 2: Especialidad correcta
        self.assertTrue(doc.edad >= 18)                # Validación 3: Es mayor de edad

    # 3 Validaciones para el modelo Paciente
    def test_paciente_validaciones(self):
        pac = Paciente.objects.get(nombre="Lucas")
        self.assertEqual(pac.apellido, "Soto")         # Validación 1: Apellido correcto
        self.assertIn("Lucas", str(pac))               # Validación 2: El nombre está en el __str__
        self.assertEqual(pac.edad, 10)                 # Validación 3: Edad correcta