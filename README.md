# AI Weather Assistant

A simple CLI application that uses Gemini tool calling to answer
weather questions using real weather data from Open-Meteo.

## Tech Stack

- Python
- Google Gemini API
- Open-Meteo API
- Requests

## How It Works

1. The user asks a question.
2. Gemini decides if it needs the weather tool.
3. The `get_weather()` function is called with the city name.
4. The function gets the city's coordinates from Open-Meteo.
5. It then gets the current weather using those coordinates.
6. The weather result is returned to Gemini.
7. Gemini gives the user a natural-language answer.

## Setup

Install the required packages:

    pip install -r requirements.txt

Create a `.env` file and add:

    GEMINI_API_KEY=your_api_key_here

Then run:

    python main.py
