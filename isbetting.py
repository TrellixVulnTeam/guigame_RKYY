import requests,json,time,numpy,pyautogui,os
from columnar import columnar
from click import  style
from rd import make_data
from sklearn import tree
clf = tree.DecisionTreeClassifier()

from readcsv import add_dataframe


##########____________Pyautogui,________________________

def make_predict():
    global predict
    data,label,test = make_data()
    predict =  convert_predict(clf.fit(data,label).predict(test)[0])
    print("make_predict v2",predict)
    add_line()

def quit_game(mes):
    import sys
    sys.exit(mes)
    
def calculate(moneys ):
    numbervnd100 = moneys//100
    moneys = moneys%100
    numbervnd50 = moneys//50
    moneys = moneys%50
    numbervnd10 = moneys//10 
    return numbervnd100,numbervnd50,numbervnd10

def get_index(name):
    confirm = input("Is {} in this position?".format(name))
    if confirm == "":
        print(pyautogui.position())
        return pyautogui.position()
    return None

def moveclick_and_moveclicks(index1,index2,number2):
    pyautogui.moveTo(index1)
    pyautogui.click()

    pyautogui.moveTo(index2)
    pyautogui.click(clicks = number2,interval=2 )

def bets():
    global predict,moneys,indexBIG,indexSMALL,indexVND10K,indexVND50K,indexVND100K
    if moneys == 0 or predict == None:
        return
    numbervnd100,numbervnd50,numbervnd10 = calculate(moneys)
    if predict == "BIG":
        index = indexBIG
    else:
        index = indexSMALL
    moveclick_and_moveclicks(indexVND100K,index,numbervnd100)
    moveclick_and_moveclicks(indexVND50K,index,numbervnd50)
    moveclick_and_moveclicks(indexVND10K,index,numbervnd10)


##########____________API________________________
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

def get_the_last_json():

    return get_json_150()[1]

def is_newgame():
    global idgame
    newid = get_id(get_json_1())
    if newid - idgame  == 1:
        idgame = newid
        time.sleep(2)
        return True
    time.sleep(5)
    return is_newgame()

##########____________PREDICT________________________







def check_predict_and_result():
    print("check_predict_and_result...")
    global predict,profits,idgame

    if predict == None:
        return

    isTrue = False
    last_js =  get_the_last_json()
    if get_id(last_js) != idgame-1:
        quit_game("da xay ra loi ket qua khong lien tuc")

    resultRaw = get_resultRaw(last_js)
    betTypeResult = get_betTypeResult(last_js)
    if predict in  betTypeResult:
        profits +=1
        isTrue = True
    else:
        profits -=1
    
    fix_line(isTrue,resultRaw,betTypeResult)


def convert_predict(number):
    if number == 1:
        return "BIG"
    return "SMALL"



    ####

def draw_screen():
    global table
    headers = ["index","id","predict","moneys","resutl","bettype","profits"]
    # os.system("clear")
    os.system("cls")
    print(columnar(table, headers, justify="c",no_borders=True))
    print("waiting...")


def add_line():
    global table,predict,moneys,idgame
    table.append([len(table),idgame,predict,moneys,"","",""])
    draw_screen()
def fix_line(isTrue,resultRaw,betTypeResult):
    global table,profits
    if isTrue:
        color = "green"
    else:
        color = "red"
    table[-1][4] = f"{style(resultRaw,fg=color)}"
    table[-1][5] = f"{style(betTypeResult,fg=color)}"
    table[-1][6] = f"{style(profits,fg=color)}"
    draw_screen()





###########################



try:
    moneys = int(input("moneys: "))
    indexBIG = get_index("BIG")
    indexSMALL = get_index("SMALL")
    indexVND10K = get_index("VND10K")
    indexVND50K = get_index("VND50K")
    indexVND100K = get_index("VND100K")
except:
    moneys = 0


table = []
js = get_json_1()
idgame = get_id(js)
timeBetCountdown = get_timeBetCountdown(js)
print(idgame,timeBetCountdown)
predict = None
if timeBetCountdown>15:
    make_predict()
    time.sleep(get_timeBetCountdown(get_json_1()))
else:
    time.sleep(timeBetCountdown)
profits = 0 
while True:
    if is_newgame():
        check_predict_and_result()
        make_predict()
        add_dataframe()
        bets()
        time.sleep(get_timeBetCountdown(get_json_1()))
