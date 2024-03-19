from picamera2 import Picamera2
import requests
import time

start_time = time.time()

capture_start_time = time.time()

picam2 = Picamera2()

camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)

picam2.start()

time.sleep(2)

# Time taken for capturing the picture
picam2.capture_file("images/imtest.jpg")

picam2.close()

capture_end_time = time.time()

# Calculate time taken for capturing the picture
capture_time = capture_end_time - capture_start_time
print(f"Time taken for capturing the picture: {capture_time:.2f} seconds")

# HTTP REST method URL
server_ip = "10.42.0.1"
port = "8888"

url = f'http://{server_ip}:{port}/result'
#print(url)

send_start_time = time.time()

# Read the image file
with open("images/imtest.jpg", "rb") as f:
    files = {'image': f}

    # Time taken for sending the image file
    # Send POST request to the HTTP endpoint
    response = requests.post(url, files=files)

send_end_time = time.time()

# Calculate time taken for sending the image file
send_time = send_end_time - send_start_time
print(f"Time taken for sending the image file: {send_time:.2f} seconds")

# Print the result
print(response.text)

# Total time taken for the entire process
end_time = time.time()
total_time = end_time - start_time
print(f"Total time taken: {total_time:.2f} seconds")
