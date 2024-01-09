from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect


def index(request):
    return render(request, 'LandingPage/index.html')

@csrf_protect
def send_contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['correo_reserva']
            subject = f"Nuevo mensaje de contacto de {email}"
            message = f"Recibiste un nuevo mensaje de contacto en tu sitio web:\n\n"    
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            return JsonResponse({'status': 'success', 'message': 'Correo enviado satisfactoriamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Formulario inválido.'})