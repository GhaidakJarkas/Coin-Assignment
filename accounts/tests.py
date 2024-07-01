from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class TestUser(APITestCase):
    def setUp(self):
        
        self.register_url = reverse('register')
        self.login_url = reverse('login')


    def test_register(self):
        data = {
            "email": "test@test.com",
            "password1": "testing321",
            "password2": "testing321"
        }

        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['message'], 'User registered successfully')
        self.assertTrue(CustomUser.objects.filter(email='test@test.com').exists())

    def test_login(self):

        user_data = {
            "email": "testlogin@test.com",
            "password1": "testing321",
            "password2": "testing321"
        }

        self.client.post(self.register_url, user_data, format='json')

        login_data = {
            "email": "testlogin@test.com",
            "password": "testing321"
        }

        response = self.client.post(self.login_url, login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


