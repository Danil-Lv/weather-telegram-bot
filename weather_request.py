import requests
from os import getenv
from dotenv import load_dotenv


def get_weather(city):
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={getenv("TOKEN_WEATHER")}&units=metric')
    return res.json()


def main():
    load_dotenv()
    get_weather()


if __name__ == '__main__':
    main()
else:
    load_dotenv()
