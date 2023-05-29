from django.shortcuts import render, redirect
from . import models as cloud1_models
from .forms import *
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_model = form.save()
            print("!!!!!!!!!!!!!", contact_model, form.save())
            contacter_name = contact_model.name
            contacter_email = contact_model.email
            contacter_message = contact_model.message
            contacter_service = contact_model.service
            subject = "Cloud One Developers"
            message = f"Dear {contacter_name},\n\nWe have received your message to avail our {contacter_service} service. This is our auto-generated response we will get back to you shortly."
            send_mail(
                subject,
                message,
                'tm825141@gmail.com',
                [contacter_email],
                fail_silently=True,
            )
            mail = Email.objects.create(contact=contact_model, mail=contacter_email, message=contacter_message)
            return redirect('home')

    form = ContactForm()
    form.fields['service'].choices = [('Select A Service:', 'Select A Service:')] + cloud1_models.service_choices
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
