import os
from dotenv import load_dotenv
from langchain_core.tools import tool  # 1. Lowercase 'tool'
import requests

load_dotenv()


@tool
def get_exchange_rate(source_curr: str, target_currency: str) -> float:
  """Fetch the current exchange rate between a source currency and a target currency (e.g., 'USD' to 'INR')."""  # 2. Required docstring

  api_key = os.getenv("EXCHANGE-API-KEY" )  # 4. Ensure this matches your .env file

  # 3. Added '/pair/' and wrapped variables in {}
  url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_curr}/{target_currency}"

  response = requests.get(url)
  data = response.json()

  # 5. Return the float rate so it matches '-> float'
  return data["conversion_rate"]

result  = get_exchange_rate.invoke({'source_curr': 'EUR', 'target_currency':'INR'})

print(result)