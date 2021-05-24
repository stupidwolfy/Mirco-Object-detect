import requests
import cv2

class WebRequest:
    def __init__(self, url):
        self.url = url

    def sendPost(self, data, imencoded):
        file = {'file': ('image.jpg', imencoded.tostring(), 'image/jpeg', {'Expires': '0'})}
        response  = requests.post(self.url, data=data, files=file, timeout=5)
        return response