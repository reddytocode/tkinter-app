import requests
import base64
import io
from PIL import Image
from CurrentUserPersistance import User
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

    @staticmethod
    def saveUser(user):
        ip = "http://127.0.0.1"
        path = "{}:5002/user/save".format(ip)
        data = user.to_json()
        print(data)
        req = requests.post(path, json=data)
        print(req.status_code)

    @staticmethod
    def get_all():
        ip = "http://127.0.0.1"
        path = "{}:5002/users".format(ip)
        req = requests.get(path)
        res = []
        if(req.status_code == 200):
            import json
            cache = json.loads(req.content)["users"]
            for user in cache:
                new_user = User()
                new_user.create(**user)
                res.append(new_user)
            return res
        else:
            return None


if __name__ == '__main__':
    # from CurrentUserPersistance import User
    # user = User()
    # Network.saveUser(user)
    Network.get_all()

