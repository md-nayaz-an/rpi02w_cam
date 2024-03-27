from gpiozero import Button
from picamera2 import Picamera2
import requests
import time
import os

class CameraController:
    def __init__(self):
        self.picam2 = self.configure_camera()

    def configure_camera(self):
        picam2 = Picamera2()
        camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
        picam2.configure(camera_config)
        picam2.start()
        return picam2

    def capture_image(self):
        time.sleep(2)
        image_path = 'images/imtest.jpg'
        self.picam2.capture_file(image_path)
        print("Image saved")
        return image_path

    def send_image(self, image_path, server_ip='10.42.0.1', port=8888):
        url = f'http://{server_ip}:{port}/result'
        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = requests.post(url, files=files)
        return response.text
    def get_audio(self, audio_path, server_ip='10.42.0.1', port=8888):
        url = f'http://{server_ip}:{port}/result-audio'
        with open(audio_path, 'wb') as f:
            response = requests.get(url)
            f.write(response.content)
        print("audio file fetched")
        os.system(f'XDG_RUNTIME_DIR=/run/user/1000 aplay {audio_path}')

def main():
    controller = CameraController()
    button = Button(2)

    def capture_and_send():
        print("Pressed")
        image_path = controller.capture_image()
        response_text = controller.send_image(image_path)
        print(response_text)
        controller.get_audio("output.wav")

    button.when_pressed = capture_and_send
    print("Press the button to capture and send an image...")

    # This keeps the script running until it's interrupted
    while True:
        try:
            # Sleep to avoid high CPU usage
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
