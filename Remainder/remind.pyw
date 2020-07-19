import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title='Remainder',
            message="It\'s time to drink water and look somewhere",
            app_icon="eye-solid.ico",
            timeout=20
        )
        time.sleep(1800)
