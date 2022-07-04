import requests
import json
import time


URL =  "https://api-csn-sun.gameland.vip/api/v1/round/ended?limit=150&page=1&tableId=103"

def number_to_result(number):
    if number>10:
        return "BIG"
    return "SMALL"
def get_response():
    global URL
    #try:
    return requests.get(URL)
    # except nameError:
    #     print(nameError)
    #     return get_response()

def get_json():
    global URL
    return json.loads(requests.get(URL).text)


def get_history_result():# return [10,14,5,7,16]
    history_list = get_json()["content"]
    history = []
    for i in range(len(history_list)-1,0,-1):
        kq = history_list[i]["resultRaw"]
        history.append(int(kq[0])+int(kq[2])+int(kq[4]))
    return history

def make_data(lenrecord):
    history = get_history_result()
    data = []
    label = []
    for i in range(len(history)-lenrecord):
        data.append(history[i:i+lenrecord])
    #     label.append(history[i+lenrecord])
        label.append(number_to_result(history[i+lenrecord]))
    dt = history[len(history)-lenrecord:len(history)]
    return data,label,[dt]

def make_data_v2(lenrecord):
    history = get_history_result()
    data = []
    label = []
    for i in range(len(history)-lenrecord):
        data.append(history[i:i+lenrecord])
        label.append(history[i+lenrecord])
    dt = history[len(history)-lenrecord:len(history)]
    return data,label,[dt]


class Record:
    index = 0
    id = 0
    def __init__(self,id,resultRaw,betTypeResult):
        self.id = id
        self.resultRaw = resultRaw
        self.betTypeResult = betTypeResult

        if Record.index !=0:
            if self.id - Record.id !=1:
                import sys
                sys.exit("da xay ra loi ket qua khong lien tiep")
        Record.index +=1
        Record.id = self.id


def create_record():
    js = get_json()
    while "resultRaw" not in js["content"][0]:
        js = get_json()
        time.sleep(1)

    rc = Record(js["content"][0]["id"],
        js["content"][0]["resultRaw"],
        js["content"][0]["betTypeResult"])
    return rc
def is_betting():
    return get_json()["content"][0]["status"] == "BETTING"

def is_ended():
    return get_json()["content"][0]["status"] == "ENDED"

def new_game():
    print("Doi van moi...")
    while True:
        if is_ended():
            while True:
                if is_betting():
                    return True
                time.sleep(1)
        time.sleep(1)


# print(get_json())
# print(get_response())