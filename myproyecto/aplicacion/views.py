from django.shortcuts import render
from .forms import PrimaryContactForm, SecondaryContactForm
from django.db import connections
from django.http import JsonResponse

def contact_view(request):
    if request.method == 'POST':
        primary_form = PrimaryContactForm(request.POST, prefix='primary')
        secondary_form = SecondaryContactForm(request.POST, prefix='secondary')
        
        if primary_form.is_valid() and secondary_form.is_valid():
            primary_form.save()  # Guarda en la base de datos por defecto
            secondary_form.save(using='secondary')  # Guarda en la base de datos secundaria
    else:
        primary_form = PrimaryContactForm(prefix='primary')
        secondary_form = SecondaryContactForm(prefix='secondary')
    
    return render(request, 'contact.html', {
        'primary_form': primary_form,
        'secondary_form': secondary_form
    })
    