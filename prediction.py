from sklearn import tree

from getAPI import make_data,make_data_v2

def predict_by_decisiontree(X_train,Y_train,X_test,rand = None):
    clf = tree.DecisionTreeClassifier(random_state=rand)
    clf.fit(X_train, Y_train)
    return clf.predict(X_test)[0]


def make_predict():
    big = 0
    small = 0
    for i in range(10,50,5):
        X_train,Y_train,X_test = make_data(i)
        predict = predict_by_decisiontree(X_train,Y_train,X_test)
        if predict == "BIG":
            big += 1
        else:
            small += 1
    if 0.7*big>small:
        return "BIG"
    elif 0.7*small:
        return "SMALL"
    else:
        return ""


def work_with_list(listt):
    models = []
    while len(models)<2:
        top = max(listt)
        index = listt.index(top)
        models.append([index,top])
        listt[index] = -1
    return models

def number_to_string(number):
    if number>10:
        return "BIG"
    return "SMALL"

# def number_to_string(number):
#     if number>10:
#         return "SMALL"
#     return "BIG"

def is_same_choice(number1,number2):
    if (number1>10 and number2>10) or (number1<=10 and number2<=10):
        return True
    return False
# def make_predict_v2():
#     sample_space = [0 for i in range(19)]

#     for i in range(5,50,1):
#         X_train,Y_train,X_test = make_data_v2(i)
#         sample_space[predict_by_decisiontree(X_train,Y_train,X_test)] +=1

#     # print(sample_space)
#     models = work_with_list(sample_space)
#     # print(models)
#     index1 = models[0][0]
#     index2 = models[1][0]
#     numof1 = models[0][1]
#     numof2 = models[1][1]

#     if is_same_choice(index1,index2):
#         # print("same")
#         return number_to_string(index1)
#     if 0.7*numof1 >numof2:
#         # print("0.7 ",index1)
#         return number_to_string(index1)
#     if 0.7*numof2 >numof1:
#         # print("0.7 ",index2)
#         return number_to_string(index2)
#     # print("no")
#     return ''



def create_random_state():
    def make_data_s(history,lenrecord):
        data = []
        label = []
        for i in range(len(history)-lenrecord):
            data.append(history[i:i+lenrecord])
        #     label.append(history[i+lenrecord])
            label.append(number_to_string(history[i+lenrecord]))
        dt = history[len(history)-lenrecord:len(history)]
        return data,label,[dt]

    def make_score(random_state,X_train,Y_train,X_score,Y_score):
        clf = tree.DecisionTreeClassifier(random_state=random_state)
        return clf.fit(X_train, Y_train).score(X_score,Y_score)
    ####################################
    from getAPI import get_history_result
    history = get_history_result()

    headed = history[0:len(history)-20]
    ended = history[len(history)-20:len(history)]

    X_train,Y_train,X_test = make_data_s(headed,10)
    X_score,Y_score,score = make_data_s(ended,10)

    L = []
    for random_state in range(100):
        score = make_score(random_state,X_train,Y_train,X_score,Y_score)
        L.append(score)

    m = max(L)
    rds = []

    for random_state in range(100):
        if L[random_state] == m:
            rds.append(random_state)
    print("max score: ",m)
    return rds

def make_predict_v2():
    random_state_s = create_random_state()
    print(random_state_s)
    X_train,Y_train,X_test = make_data(10)

    b = 0
    s = 0
    for random_state in random_state_s:
        predict = predict_by_decisiontree(X_train,Y_train,X_test,random_state)
        if predict == "BIG":
            b+=1
        if predict == "SMALL":
            s+=1
    if b>s:
        return "BIG"
    elif s>b:
        return "SMALL"
    return ""
