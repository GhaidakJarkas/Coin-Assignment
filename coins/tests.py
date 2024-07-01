from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model

from coins.models import Coin


class CoinTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='testuser@test.com', password='testpassword')

        self.coin1 = Coin.objects.create(name='Bitcoin', symbol='BTC', price=30000)
        self.coin2 = Coin.objects.create(name='Ethereum', symbol='ETH', price=2000)

        self.token = self.get_token_for_user('testuser@test.com', 'testpassword')
        self.url = reverse('coins')

    def get_token_for_user(self, email, password):
        url = reverse('login')
        response = self.client.post(url, {'email': email, 'password': password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_get_coins_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Bitcoin')
        self.assertEqual(response.data[1]['name'], 'Ethereum')

    def test_post_coin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        data = {
            'name': 'Litecoin',
            'symbol': 'LTC',
            'price': 150
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Coin added successfully')

        self.assertEqual(Coin.objects.count(), 3)
        self.assertEqual(Coin.objects.get(name='Litecoin').symbol, 'LTC')
