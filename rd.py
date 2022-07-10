import requests,json,numpy

def get_json_1():
    # print("get_json_1")
    URL = "https://api-csn-sun.gameland.vip/api/v1/round/running?"
    js = json.loads(requests.get(URL).text)
    if js == []:
        time.sleep(1)
        return get_json_1()
    return js[0]

def get_json_150():
    URL =  "https://api-csn-sun.gameland.vip/api/v1/round/ended?limit=150&page=1&tableId=103"
    return json.loads(requests.get(URL).text)["content"]

def get_id(js):
    return int(js["id"])

def get_resultRaw(js):
    if "resultRaw" in js:
        return js["resultRaw"]
    return ""

def get_betTypeResult(js):
    if "betTypeResult" in js:
        return js["betTypeResult"]
    return ""

def get_status(js):
    return js["status"]

def get_timeBetCountdown(js):
    return js["timeBetCountdown"]

def get_dealerName(js):
    return js["dealerName"]

# def get_history_by_id(id):
#     js150 = get_json_150()
#     newid = get_id(js150[0])
#     index = newid - id 

#     history = []

#     while index<150 and len(history)<5:
#         history.append(get_resultRaw(js150[index]))
#         index +=1

#     return history


class Match:
    def __init__(self,js):
        self.id = get_id(js)
        self.dealerName = get_dealerName(js)
        self.resultRaw = get_resultRaw(js)
        self.betTypeResult = get_betTypeResult(js)
    def show(self):
        print(self.id,self.dealerName,self.resultRaw,self.betTypeResult,self.history)

    def get_info(self):
        return [self.id,self.dealerName,self.resultRaw,self.betTypeResult,self.history]
def create_Time():
    Time = []
    js150 = get_json_150()
    for js in js150:
        match = Match(js)
        Time.append(match)
    Time.reverse()
    return Time

def show_time(Time):
    for match in Time:
        match.show()

Time = create_Time()

show_time(Time)


