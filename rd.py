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

# def convert_predict(number):
#     if number == 1:
#         return "BIG"
#     return "SMALL"


def number_to_predict(number):
    if number>10:
        return 1
    return 0
def string_to_number_result(string):
    return int(string[0])+int(string[2])+int(string[4])

def make_line(js150,i):
        global  dealerNameList
        id = get_id(js150[i])
        dealerName = get_dealerName(js150[i])
        if dealerName in dealerNameList:
            index = dealerNameList.index(dealerName)
        else:
            index = len(dealerNameList)-1
            dealerNameList.append(dealerName)
        ######van truoc
        resultRaw = get_resultRaw(js150[i+1])
        # betTypeResult = get_betTypeResult(js150[i+1])
        l2 = string_to_number_result(get_resultRaw(js150[i+2]))
        l3 = string_to_number_result(get_resultRaw(js150[i+3]))
        l4 = string_to_number_result(get_resultRaw(js150[i+4]))
        l5 = string_to_number_result(get_resultRaw(js150[i+5]))
        l6 = string_to_number_result(get_resultRaw(js150[i+6]))
        return numpy.array([id,index,int(resultRaw[0]),int(resultRaw[2]),int(resultRaw[4]),l2,l3,l4,l5,l6])

def make_data():
    data = []
    label = []
    js150 = get_json_150()

    for i in range(len(js150)-7,0,-1):
        data.append( make_line(js150,i))
        label.append(number_to_predict(string_to_number_result(get_resultRaw(js150[i]))))
    test = [make_line(js150,0)]
    return data,label,test



dealerNameList = []
