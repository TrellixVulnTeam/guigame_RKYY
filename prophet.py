from sklearn.tree import DecisionTreeClassifier

from getAPI import make_data

def predict_by_decisiontree(X_train,Y_train,X_test,random_state=100,max_depth=10):
    tree = DecisionTreeClassifier(criterion = "gini",random_state = random_state,max_depth=max_depth, min_samples_leaf=5)
    return tree.fit(X_train,Y_train).predict(X_test)[0]



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
    if big == small:
        return ""
    if big>small:
        return "BIG"
    return "SMALL"
