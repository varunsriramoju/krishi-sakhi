import os, requests
OPENWEATHER_KEY = os.getenv('OPENWEATHER_KEY', None)

def get_weather_by_location(lat=None, lon=None, q=None):
    # For demo: use OpenWeather if key present; otherwise return static sample
    if OPENWEATHER_KEY and (lat and lon):
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_KEY}&units=metric'
        r = requests.get(url)
        return r.json()
    # static sample (no external calls)
    return {'forecast':'No API key. Sample: rain expected tomorrow.'}
