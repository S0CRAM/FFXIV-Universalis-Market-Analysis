import requests

class marketAPI:
    def __init__(self, ID):
        pass
    def sales(self,item_id):
        URL = 'https://universalis.app/api/history/primal/' + item_id


    def itemName(self, item_id):
        URL = 'https://raw.githubusercontent.com/Universalis-FFXIV/Universalis/v1/public/json/itemNameIds.json'
        item_D = requests.get(URL).json()
        item_name = item_D[item_id]
        return item_name