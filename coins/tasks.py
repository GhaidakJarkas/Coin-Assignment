from celery import shared_task
import requests

from .models import Coin



@shared_task()
def update_price():
    coins = Coin.objects.all()
    
    for coin in coins:
        url = f'https://api.tokenncoin.com/exchanges/get-pair?exchange=MEXC&pair={coin.symbol}/USDT'
        try:
            response = requests.get(url)
            response.raise_for_status() 
            try:
                result = response.json()
                print(result)
                price = result.get("price")
                print(price)
                coin.price = price
                coin.save()
            except requests.exceptions.JSONDecodeError:
                print(f"Error decoding JSON response for coin: {coin.symbol}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for coin: {coin.symbol}, error: {e}")

