import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.messages import get_messages

from authentication.models import User

@pytest.mark.test_authentication_view
@pytest.mark.parametrize(
    "first_name, last_name, username, email, password1, password2, status_code",
    [
        ("John", "Doe", "johndoe123", "john.doe@example.com", "StrongP@ssword1", "StrongP@ssword1", 302),
        ("Alice", "Smith", "alicesmith", "test.smith@example.com", "SecurePwd123", "SecurePwd123", 200),  # Bad Request (Username already exists)
        ("Alex", "Smith", "alexsmith", "alex.smith@example.com", "SecurePwd144", "SecurePwd144", 200),  # Bad Request (Email already exists)
        ("Bob", "Johnson", "bob123", "invalid_email", "Passw0rd!", "Passw0rd!", 200), # Bad Request (Invalid email format)
        ("Eva", "Williams", "evawill", "eva.williams@example.com", "Secure123!", "MismatchedPwd456", 200), # Bad Request (Passwords do not match)
        ("Michael", "", "michael88", "michael@example.com", "StrongPassword123", "StrongPassword123", 200), # Bad Request (Last name is required)
        ("Laura", "Clark", "laura22", "laura.clark@example.com", "ShortPw", "ShortPw", 200), # Bad Request (Password must be at least 8 characters)
        ("", "Johnson", "user123", "user@example.com", "SecurePassword123", "SecurePassword123", 200), # Bad Request (First name is required)
    ]
)
def test_authentication_view_singup_POST(db, first_name, last_name, username, email, password1, password2, status_code, custom_user_factory):
    client = Client()
    custom_user_factory.create(username="alicesmith") #user with username exists
    custom_user_factory.create(email="alex.smith@example.com") #user with email exists
    amount_users = User.objects.count()
    sign_up_form_data = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'email': email,
        'password1': password1,
        'password2': password2,
    }

    url = reverse('signup')
    response = client.post(url, sign_up_form_data)

    if status_code != 200:
        amount_users += 1 
    assert response.status_code == status_code
    assert User.objects.count() == amount_users


@pytest.mark.test_authentication_view
def test_authentication_view_user_login_POST(db):
    client = Client()
    user = User.objects.create_user(first_name="firstname", 
                                    last_name="lastname", 
                                    email="test@test.com", 
                                    username="testuser", 
                                    password="test_password", 
                                    is_email_verified=True)
    login_user_data = {
        'username': "testuser",
        'password': "test_password",
    }
    print(user.username, user.password)
    url = reverse('login')
    response = client.post(url, data=login_user_data)

    assert response.status_code == 302
    assert response.url == reverse('frontpage')

    user.is_email_verified = False
    user.save()
    response = client.post(url, login_user_data)
    
    assert response.status_code == 302
    assert response.url == reverse('login')