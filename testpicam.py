from picamera2 import Picamera2, Preview
import requests
import time

picam2 = Picamera2()

camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)

#picam2.start_preview(Preview.QTGL)

picam2.start()

time.sleep(2)

picam2.capture_file("imtest.jpg")

picam2.close()

# HTTP REST method URL
server_ip = "192.168.188.217"
port = "8888"

url = f'https://{server_ip}:{port}/result'
print(url)
# Read the image file
with open("imtest.jpg", "rb") as f:
    files = {'image': f}

    # Send POST request to the HTTP endpoint
    response = requests.post(url, files=files)

# Print the result
print(response.text)
