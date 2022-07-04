from sklearn import tree
clf = tree.DecisionTreeClassifier()

from getAPI import make_data,make_data_v2

def predict_by_decisiontree(X_train,Y_train,X_test):
    clf.fit(X_train, Y_train)
    return clf.predict(X_test)[0]



def string_to_result(strings):
    if "BIG" in strings:
        return "BIG"
    return "SMALL"





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

def is_same_choice(number1,number2):
    if (number1>10 and number2>10) or (number1<=10 and number2<=10):
        return True
    return False
def make_predict_v2():
    sample_space = [0 for i in range(19)]

    for i in range(5,50,1):
        X_train,Y_train,X_test = make_data_v2(i)
        sample_space[predict_by_decisiontree(X_train,Y_train,X_test)] +=1

    # print(sample_space)
    models = work_with_list(sample_space)
    # print(models)
    index1 = models[0][0]
    index2 = models[1][0]
    numof1 = models[0][1]
    numof2 = models[1][1]

    if is_same_choice(index1,index2):
        # print("same")
        return number_to_string(index1)
    if 0.7*numof1 >numof2:
        # print("0.7 ",index1)
        return number_to_string(index1)
    if 0.7*numof2 >numof1:
        # print("0.7 ",index2)
        return number_to_string(index2)
    # print("no")
    return ''



