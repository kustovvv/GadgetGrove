from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            template = render_to_string('core/email_template.html', {'name': form.cleaned_data['first_name']})
        
            email = EmailMessage(
                'Thank you for registering to our site!',
                template,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
            )

            email.fail_silently=False
            email.send()

            user = form.save()
            login(request, user)
            

            return redirect('frontpage')
    else:
        form = SignUpForm()

    request.session['navbar_state'] = 'hidden'

    return render(request, 'authentication/signup.html', {'form': form})
