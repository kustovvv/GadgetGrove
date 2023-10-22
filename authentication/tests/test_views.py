from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

class TestViews(TestCase):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('authentication:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/signup.html")

    def test_should_show_login_page(self):
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_should_signup_user(self):
        self.user = {
            "first_name": "first",
            "last_name": "last",
            "username": "Ihor",
            "email": "zegorovsky1355@hmail.com",
            "password1": "ddbs3421",
            "password2": "ddbs3421"
        }

        response = self.client.post(reverse("authentication:signup"), self.user)
        self.assertEquals(response.status_code, 302)

    # def test_should_not_signup_user_with_taken_username(self):
    #     self.user = {
    #         "first_name": "first",
    #         "last_name": "last",
    #         "username": "Ihor",
    #         "email": "zegorovsky1355@12mail.com",
    #         "password1": "ddbs3421",
    #         "password2": "ddbs3421"
    #     }

    #     self.client.post(reverse("authentication:signup"), self.user)
    #     response = self.client.post(reverse("authentication:signup"), self.user)
    #     self.assertEquals(response.status_code, 409)

    #     storage = get_messages(response.wsgi_request)

    #     for message in storage:
    #         print(message)

    #     import pdb
    #     pdb.set_trace()

    
    # def test_should_not_signup_user_with_taken_email(self):
    #     self.user = {
    #         "first_name": "first",
    #         "last_name": "last",
    #         "username": "username1",
    #         "email": "zegorovsky1355@mail2.com",
    #         "password1": "ddbs3421",
    #         "password2": "ddbs3421"
    #     }

    #     self.test_user2 = {
    #         "first_name": "first",
    #         "last_name": "last",
    #         "username": "username22",
    #         "email": "zegorovsky1355@mail2.com",
    #         "password1": "ddbs3421",
    #         "password2": "ddbs3421"
    #     }

    #     self.client.post(reverse("authentication:signup"), self.user)
    #     response = self.client.post(reverse("authentication:signup"), self.test_user2)
    #     self.assertEquals(response.status_code, 409)

