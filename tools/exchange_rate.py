import os
from dotenv import load_dotenv
import requests

load_dotenv()

# 1. Fetch the key from your .env file (make sure the variable name matches your .env)
api_key = os.getenv("EXCHANGE-API-KEY")

# 2. Use an f-string (f'...') to inject the variable into the URL
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)