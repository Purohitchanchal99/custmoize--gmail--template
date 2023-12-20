from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            html_message = render_to_string('emails/EMAILTEMPLATE.HTML', {
                'name': name,
                'email': email,
            })

            subject = 'The contact form subject'

            # Send email to the user's entered email address
            send_mail(
                subject,
                "",  # Empty string for the message since you're using html_message
                settings.EMAIL_HOST_USER,
                [email],
                html_message=html_message
            )

            # Optionally, you can also send a copy of the email to your own email address
            # send_mail(subject, "", settings.EMAIL_HOST_USER, ['your_email@example.com'], html_message=html_message)

            return redirect(reverse('index'))  # Assuming you have a URL pattern named 'index'
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })
