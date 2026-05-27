# 🌤️ Weather CLI App

A command-line weather app built with Python that fetches real-time weather data for any city worldwide.

## Features

- Real-time temperature (°C and °F)
- Feels like, humidity, wind speed & direction
- Visibility and UV index
- Error handling for invalid city, no internet, timeout
- Check multiple cities without restarting

## Setup

```bash
git clone https://github.com/samoff04/Weather-CLI-App.git
cd Weather-CLI-App
pip install -r requirements.txt
python main.py
```

## Tech Stack

- Python 3.x
- Requests library
- wttr.in API (no key required)
