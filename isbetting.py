import requests,json,time,numpy,pyautogui,os
from columnar import columnar
from click import  style
from sklearn import tree
clf = tree.DecisionTreeClassifier()


##########____________Pyautogui,________________________


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
    if self.predict == "BIG":
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


def get_history_result():# return [10,14,5,7,16]
    js150 = get_json_150()
    history = []
    for i in range(len(js150)-1,0,-1):
        kq = get_resultRaw(js150[i])
        history.append(int(kq[0])+int(kq[2])+int(kq[4]))
    return history

def make_data(lenrecord=100):
    history = get_history_result()
    data = []
    label = []
    for i in range(len(history)-lenrecord):
        data.append(history[i:i+lenrecord])
        label.append(history[i+lenrecord])
    dt = history[len(history)-lenrecord:len(history)]
    return data,label,[dt]

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

def convert_result(listt):
    for i in range(len(listt)):
        if listt[i]>10:
            listt[i] = 1
        else:
            listt[i] = 0
    return listt
def convert_predict(number):
    if number == 1:
        return "BIG"
    return "SMALL"

def make_random_data(height = 100, width = 100):
    dt_1 = numpy.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_2 = numpy.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_3 = numpy.random.default_rng().integers(low=1,high=7,size=(height,width))
    lb = numpy.random.default_rng().integers(low=0,high=2,size=(height,))
    return dt_1+dt_2+dt_3, lb

def make_predict():
    print("make_predict...")
    global predict  
    score_data, score_label,test_data = make_data()
    score_label = convert_result(score_label)
    # print(score_label)
    start = time.time()

    max_score = 0
    max_predict = 10.5
    while time.time()-start <15:

        rd_data,rd_label = make_random_data()
        clf.fit(rd_data,rd_label)
        score = clf.score(score_data,score_label)
        if score>max_score:
            max_score = score
            max_predict = clf.predict(test_data)[0]
    predict =  convert_predict(max_predict)
    add_line()
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





############################
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
if timeBetCountdown>30:
    make_predict()
    time.sleep(get_timeBetCountdown(get_json_1()))
else:
    time.sleep(timeBetCountdown)
profits = 0 
while True:
    if is_newgame():
        check_predict_and_result()
        make_predict()
        bets()
        time.sleep(get_timeBetCountdown(get_json_1()))


