import numpy as np
from getAPI import make_data_v2
from sklearn import tree
clf = tree.DecisionTreeClassifier()
import time
# clf.fit(X_train, Y_train)
# return clf.predict(X_test)[0]

####################################


def make_random_data(height = 1000, width = 100):
    dt_1 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_2 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    dt_3 = np.random.default_rng().integers(low=1,high=7,size=(height,width))
    lb_1 = np.random.default_rng().integers(low=1,high=7,size=(height,))
    lb_2 = np.random.default_rng().integers(low=1,high=7,size=(height,))
    lb_3 = np.random.default_rng().integers(low=1,high=7,size=(height,))
    return dt_1+dt_2+dt_3, lb_1+lb_2+lb_3

def number_to_string(number):
    print("number:",number)
    if number>10:
        return "BIG"
    return "SMALL"

def make_predict_v2():
    len_record = 100    
    score_data, score_label,test_data = make_data_v2(len_record)
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
    print(max_predict)
    return number_to_string(max_predict)



# def make_predict_v2():
#     len_record = 100    
#     score_data, score_label,test_data = make_data_v2(len_record)
#     l = len(score_data)
#     score_data = score_data[l-10:l]
#     score_label = score_label[l-10:l]
#     start = time.time()

#     max_score = 0
#     max_predict = 10.5
#     while time.time()-start <15:

#         rd_data,rd_label = make_random_data(height=100, width=len_record)
#         clf.fit(rd_data,rd_label)
#         score = clf.score(score_data,score_label)
#         if score>max_score:
#             max_score = score
#             max_predict = clf.predict(test_data)[0]
#             print(score,max_predict)
#     print(1/16)
#     print(max_predict)
#     return number_to_string(max_predict)
    


# print(make_predict_v2())