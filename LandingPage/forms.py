from django import forms
from django.forms import widgets

class ContactForm(forms.Form):
    TIPO_CATA_CHOICES = [
        ('normal', 'Cata Normal - Un recorrido clásico por nuestros mezcals más representativos.'),
        ('premium', 'Cata Premium - Una selección exclusiva de nuestras reservas premium y ediciones limitadas.'),
        ('con-maridaje', 'Cata con Maridaje - Una experiencia sensorial que combina nuestros mezcals con alimentos artesanales locales.'),
        ('personalizada', 'Cata Personalizada - Diseña tu propia cata con la ayuda de nuestros sommeliers.'),
        ('al-amanecer', 'Cata al Amanecer - Disfruta de la belleza del amanecer en nuestros campos mientras degustas.')
    ]

    HORARIO_CHOICES = [
        ('9', '09:00 AM'),
        ('11', '11:00 AM')
        # Agrega más horarios según sea necesario
    ]

    tipo_cata = forms.ChoiceField(choices=TIPO_CATA_CHOICES)
    fecha_reserva = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    telefono_reserva = forms.CharField(max_length=20)
    correo_reserva = forms.EmailField()
    horario_reserva = forms.ChoiceField(choices=HORARIO_CHOICES)
    nombre_reserva = forms.CharField(max_length=100)
