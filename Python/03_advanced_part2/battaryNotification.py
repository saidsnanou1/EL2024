import psutil
from plyer import notification


if __name__ == "__main__":

    # Get the battery status
    battery_status = psutil.sensors_battery()
    percent = battery_status.percent

    # send the notification
    notification.notify(
        title="Battery Percentage", message=f"{percent}% percent remaining", timeout=10
    )
