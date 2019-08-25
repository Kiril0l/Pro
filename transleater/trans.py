import requests
API_KEY = "trnsl.1.1.20190804T150138Z.57c025934003036c.fbe8fe4a100b90d3c422790abe068653ba4f8992"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"


class Trans():
    def __init__(self, *args, **kwargs):
        if kwargs.get("text") and kwargs.get("lang"):
            self.url = "{0}?text={1}&lang={2}&key={3}".format(URL, f"{kwargs['text']}", f"{kwargs['lang']}", API_KEY)
        elif kwargs.get("text"):
            self.url = "{0}?text={1}&lang=en&key={2}".format(URL, f"{kwargs['text']}", API_KEY)
        pass

    def get_date(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.result = response.json()
        else:
            self.result = {}

    def create_response(self):
        template = f"""Перевод: {self.result["text"]}.
        Языки: {self.result["lang"]}.
    """
        print(template)




if __name__ == "__main__":
    obj = Trans(text = "привет", lang = "lt")
    # print(obj.url)
    obj.get_date()
    obj.create_response()







# https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190804T150138Z.57c025934003036c.fbe8fe4a100b90d3c422790abe068653ba4f8992&text=%D0%BA%D1%83%D1%80%D0%B8%D1%82%D1%8C&lang=en&format=plain
