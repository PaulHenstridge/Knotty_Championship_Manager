import requests
import random

from utils.local_names import firsts as local_first_names
from utils.local_names import lasts as local_last_names

def generate_name():
    api_url = "https://randomuser.me/api/?gender=male"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        first_name = data["results"][0]["name"]["first"]
        last_name = data["results"][0]["name"]["last"]
        thumbnail_url = data["results"][0]["picture"]["thumbnail"]

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Thumbnail URL: {thumbnail_url}")

        return f"{first_name} {last_name}", thumbnail_url
    else:
        print("Failed to fetch data:", response.status_code)
        return {"Bobby NoNames"}

def generate_local_name():
    api_url = "https://randomuser.me/api/?gender=male"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        first_name = random.choice(local_first_names)
        last_name = random.choice(local_last_names)

        thumbnail_url = data["results"][0]["picture"]["thumbnail"]

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Thumbnail URL: {thumbnail_url}")

        return f"{first_name} {last_name}", thumbnail_url
    else:
        print("Failed to fetch data:", response.status_code)
        return {"Bobby NoNames"}