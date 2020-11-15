from datetime import datetime
import numpy as np
import cv2
#dt.strftime("%A, %d. %B %Y %I:%M%p")

def convert_time_to_string(dt):
    return f"{dt.strftime("%H:%M")"
    
def convert_date_to_string(dt):
    return f"{dt.strftime("%A, %d.%m.%y")"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background():
    #return np.zeros((500, 500))
    return cv2.imread ("2.jpg")

def generate_time_image_bytes(dt):
    time = convert_time_to_string(dt)
    date = convert_date_to_string(dt)
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, time, (int(image.shape[0]*0.12), int(image.shape[1]*0.75)), font, 2.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, date, (int(image.shape[0]*0.17), int(image.shape[1]*0.81)), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
