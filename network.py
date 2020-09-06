import requests
import base64
import io
from PIL import Image

ip = "http://104.131.122.100"


class Network:
    @staticmethod
    def tratar_imagen(path):
        img = Image.open(path).convert('RGB')
        new_path = "{}.jpg".format(path[:-4])
        img.save(new_path)
        return new_path

    @staticmethod
    def get_category(path):
        category_url = "{}:5000/category".format(ip)
        path = Network.tratar_imagen(path)
        req = requests.post(category_url, files={'file': open(path, mode='rb')})
        if req.status_code == 200:
            print("la huella es: ", req.content)
            return req.content
        else:
            return None


    @staticmethod
    def get_analisis_results(path):
        alalisis_url = "{}:5001/".format(ip)
        path = Network.tratar_imagen(path)
        req = requests.post(alalisis_url, files={'file': open(path, mode='rb')})
        if(req.status_code == 200):
            encoded_image = req.json()['encode'][2:-1]
            distance = req.json()['distance']
            # msg = base64.b64decode(encoded_image)
            # buf = io.BytesIO(msg)
            # img = Image.open(buf)
            # img.save("decoded.jpg")
            return distance, encoded_image
        else:
            return None, None
