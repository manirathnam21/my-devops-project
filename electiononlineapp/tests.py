from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_successful(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('home'))  

    def test_login_invalid_credentials(self):   
        response = self.client.post(reverse('login'), {
            'username': "wronguser",
            'password': "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "Invalid username or password")

    def test_login_blank_fields(self):
        response = self.client.post(reverse('login'), {
            'username': "",
            'password': ""
        })
        self.assertEqual(response.status_code, 200)  

    def test_login_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200) 
