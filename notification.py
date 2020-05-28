import time
from plyer import notification

while True:
    notification.notify(title = 'PLEASE DRINK WATER!! :)', message = 'Regularly Drinking Water is good for Health!',app_icon = 'drink.ico', timeout = 10)
    time.sleep(60)