import requests
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def get_weather(city: str):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(geo_url, params=geo_params)

    if response.status_code != 200:
        return {"error": "Could not get city information."}

    data = response.json()

    if "results" not in data:
        return {"error": f"Could not find the city {city}."}

    location = data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
    }

    response = requests.get(weather_url, params=weather_params)

    if response.status_code != 200:
        return {"error": "Could not get weather information."}

    weather_data = response.json()

    current = weather_data["current_weather"]

    return {
        "city": city,
        "temperature_c": current["temperature"],
        "wind_speed_kmh": current["windspeed"]
    }


def main():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Please add GEMINI_API_KEY to your .env file.")
        return

    client = genai.Client(api_key=api_key)

    config = types.GenerateContentConfig(
        tools=[get_weather]
    )

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=config
    )

    print("AI Weather Assistant")
    print("Ask me about the weather!")
    print("Type 'quit' to exit.")

    while True:

        question = input("\nYou: ")

        if question.lower() == "quit":
            print("Goodbye!")
            break

        try:
            response = chat.send_message(question)
            print("Assistant:", response.text)

        except Exception as e:
            print("Something went wrong:", e)


if __name__ == "__main__":
    main()
