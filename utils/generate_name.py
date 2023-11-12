import requests

def generate_name():
    api_url = "https://randomuser.me/api/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        first_name = data["results"][0]["name"]["first"]
        last_name = data["results"][0]["name"]["last"]
        thumbnail_url = data["results"][0]["picture"]["thumbnail"]

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Thumbnail URL: {thumbnail_url}")

        return f"{first_name} {last_name}"
    else:
        print("Failed to fetch data:", response.status_code)
        return {"Bobby NoNames"}

