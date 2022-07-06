
class Player:
    def __init__(self,moneys=0,playing=False) :
        self.predict = prediction.make_predict_v2()
        self.moneys = moneys
        self.isPlaying = playing
        self.true = 0
        self.false = 0
    def check_predict(self,betTypeResult):

        if self.predict == None or self.predict == "":
            return
        if self.predict in betTypeResult:
            self.true  +=1
        else:
            self.false+=1 
    def make_predict(self):
        self.predict = prediction.make_predict_v2()
    def bets(self):
        global indexBIG,indexSMALL,indexVND10K,indexVND50K,indexVND100K
        if self.isPlaying == False:
            return
        numbervnd100,numbervnd50,numbervnd10 = manipulation.calculate(self.moneys)
        if self.predict == "BIG":
            index = indexBIG
        elif self.predict == "SMALL":
            index = indexSMALL
        else:
            print("should not participate")
            return
        manipulation.moveclick_and_moveclicks(indexVND100K,index,numbervnd100)
        manipulation.moveclick_and_moveclicks(indexVND50K,index,numbervnd50)
        manipulation.moveclick_and_moveclicks(indexVND10K,index,numbervnd10)

def make_line(stt='',id='',predict='',moneys='',resultRaw='',betTypeResult='',history=''):
    if predict == '':
        moneys = ''
    return [stt,id,predict,moneys,resultRaw,betTypeResult,history]
def fix_line(line,properties,predict,resultRaw):
    if predict==None or predict == '':
        color = "white"
    elif predict in resultRaw:
        color="green"
    else:
        color="red"
    for i in range(len(properties)):
        if properties[i]!='':
            line[i] = f"{style(properties[i],fg=color)}"
    return line
    


#_________________________________________________________________

import manipulation,getAPI,draw #,prediction
import json,time
from click import  style
import noname as prediction

#_________________________________________________________________

try:
    moneys = int(input("moneys: "))
    indexBIG = manipulation.get_index("BIG")
    indexSMALL = manipulation.get_index("SMALL")
    indexVND10K = manipulation.get_index("VND10K")
    indexVND50K = manipulation.get_index("VND50K")
    indexVND100K = manipulation.get_index("VND100K")
    if None in [indexBIG,indexSMALL,indexVND10K,indexVND50K,indexVND100K]:
        manipulation.quit_game("cai dai that bai")
    
    if getAPI.new_game():
        Pler = Player(moneys,True)
except:
    Pler = Player()
allLines = []
HEADER = ["time","id","predict","moneys","resultRaw","betTypeResult","history"]
line = make_line(stt=len(allLines),id=getAPI.get_json()["content"][0]["id"],predict=Pler.predict,moneys=Pler.moneys)
allLines.append(line)
draw.draw_screen(allLines,HEADER)
Pler.bets()



while 1:
    record = getAPI.create_record()
    Pler.check_predict(record.betTypeResult)
    allLines[-1] = fix_line(allLines[-1],['','','','',record.resultRaw,record.betTypeResult,Pler.true-Pler.false ],Pler.predict,record.betTypeResult)
    draw.draw_screen(allLines,HEADER)
    while 1:
        if getAPI.is_betting():
            a = time.time()
            Pler.make_predict()
            line = make_line(stt=len(allLines),id=getAPI.get_json()["content"][0]["id"],predict=Pler.predict,moneys=Pler.moneys)
            allLines.append(line)
            draw.draw_screen(allLines,HEADER)
            Pler.bets()
            b = time.time()
            time.sleep(max(50-int(b-a),0))
            break




