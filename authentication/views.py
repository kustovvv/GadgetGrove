from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading

from .forms import SignUpForm, LoginForm


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('authentication/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, 
                 body=email_body, 
                 from_email=settings.EMAIL_FROM_USER,
                 to=[user.email]
                 )
    
    EmailThread(email).start()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_activation_email(user, request)

            messages.info(request, 'We sent you an email to verify your account')
            return render(request, 'authentication/login.html')

    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)

            if user.is_email_verified:            
                login(request, user)
                messages.success(request, f'Welcome {user.username}')

                return redirect('frontpage')
            
            else:
                messages.error(request, "You haven't verified your email, please check your email inbox.")

            return redirect('authentication:login')
        
        except Exception as e:
            messages.error(request, 'Something went wrong. Please enter correct email or password')
            
            return redirect('authentication:login')
        
    else:
        form = LoginForm()

        return render(request, 'authentication/login.html', {'form': form})


def activate_user(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)

    except Exception as e:
        user = None
        
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.success(request, 'Email verified, you can now log in.')
        return redirect(reverse('authentication:login'))
    
    return render(request, 'authentication/activate-failed.html', {'user': user})