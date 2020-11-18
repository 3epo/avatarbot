from datetime import datetime
import numpy as np
import cv2
import pyowm
from pyowm.commons.enums import SubscriptionTypeEnum
from pyowm.utils.measurables import kelvin_to_celsius

city = 'Tashkent'

config = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
        },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}

owm = pyowm.OWM('d3d48a022e1d2f6dd90197f50795a4ab', config=config)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = kelvin_to_celsius(w.temp['temp'])
temp2 = int(temp)

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
    
def convert_date_to_string(dt):
    return f"{dt.day}.{dt.month}.{dt.year}"
    
def convert_weather_to_string():
    return f"%d*"% temp2


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background():
    #return np.zeros((500, 500))
    return cv2.imread ("2.jpg")

def generate_time_image_bytes(dt):
    time = convert_time_to_string(dt)
    date = convert_date_to_string(dt)
    weather = convert_weather_to_string()
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, time, (int(image.shape[0]*0.12), int(image.shape[1]*0.75)), font, 2.5, (255, 255, 255), 2, cv2.LINE_AA),
    cv2.putText(image, date, (int(image.shape[0]*0.18), int(image.shape[1]*0.81)), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA),
    cv2.putText(image, weather, (int(image.shape[0]*0.46), int(image.shape[1]*0.67)), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
