import plyer

import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="HEADING HERE",
        message=" DESCRIPTION HERE",

        # displaying time
        timeout=4
    )
    # waiting time
    time.sleep(7)

# codes are taken from https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/