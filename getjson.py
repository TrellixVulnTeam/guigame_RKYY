import requests,json


def get_json():
    URL = "https://api-csn-sun.gameland.vip/api/v1/round/running?token=32-40c223333bbacb5f39fd573ebf95a4f0"
    return json.loads(requests.get(URL).text)

print(get_json())