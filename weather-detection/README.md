# Weather Detection

Real-time weather information GUI application using OpenWeatherMap API.

## Features
- 🌤️ Real-time weather data
- 🌡️ Temperature display
- 💨 Atmospheric pressure
- 💧 Humidity levels
- 📝 Weather description
- 🎨 Colorful GUI interface

## Requirements
```bash
pip install requests
```

## Setup

1. Get your free API key from: https://openweathermap.org/api

2. Set the environment variable:
```bash
export OPENWEATHER_API_KEY='your-api-key-here'
```

Or on Windows:
```bash
set OPENWEATHER_API_KEY=your-api-key-here
```

## Usage
```bash
python weather_detection.py
```

## How to Use
1. Enter a city name in the input field
2. Click the button to fetch weather data
3. View the weather information displayed

## Information Displayed
- **Temperature** - Current temperature in Kelvin
- **Pressure** - Atmospheric pressure in hPa
- **Humidity** - Humidity percentage
- **Description** - Weather condition description

## Interface
- Light green background
- Dark green labels
- Red header
- Entry fields for easy data display

## Error Handling
- ✅ Invalid city name detection
- ✅ API connection errors
- ✅ Clear error messages

## Note
- API key required (free tier available)
- Internet connection required
- Temperature shown in Kelvin (can be converted)
