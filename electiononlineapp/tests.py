"""Test cases for electiononlineapp login functionality."""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTestCase(TestCase):
    """Test suite for login functionality."""

    def setUp(self):
        """Create a test user for login tests."""
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_successful(self):
        """Test login with correct username and password."""
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('home'))

    def test_login_invalid_credentials(self):
        """Test login with incorrect username and password."""
        response = self.client.post(reverse('login'), {
            'username': "wronguser",
            'password': "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password")

    def test_login_blank_fields(self):
        """Test login with blank username and password."""
        response = self.client.post(reverse('login'), {
            'username': "",
            'password': ""
        })
        self.assertEqual(response.status_code, 200)

    def test_login_get_request(self):
        """Test accessing login page using GET request."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        