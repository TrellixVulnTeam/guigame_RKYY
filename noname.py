import numpy as np
from getAPI import make_data_v2
from sklearn import tree
clf = tree.DecisionTreeClassifier()
import time


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

def make_random_data(height = 1000, width = 100):
    dt_1 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_2 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_3 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    lb = np.random.default_rng().integers(low=0,high=2,size=(height,))
    return dt_1+dt_2+dt_3, lb

def make_predict_v2():
    len_record = 100    
    score_data, score_label,test_data = make_data_v2(len_record)
    score_label = convert_result(score_label)
    # print(score_label)
    start = time.time()

    max_score = 0
    max_predict = 10.5
    while time.time()-start <15:

        rd_data,rd_label = make_random_data(height=100, width=len_record)
        clf.fit(rd_data,rd_label)
        score = clf.score(score_data,score_label)
        if score>max_score:
            max_score = score
            max_predict = clf.predict(test_data)[0]
    return convert_predict(max_predict)


