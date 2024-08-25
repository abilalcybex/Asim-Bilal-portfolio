from plyer import notification
import time

def show_toast(title, message, duration=5):
    notification.notify(
        title=title,
        message=message,
        timeout=duration,
    )

if __name__ == "__main__":
    title = "Employee Tracking"
    message = "Focus on your work please, you are being recorded."
    show_toast(title, message)
