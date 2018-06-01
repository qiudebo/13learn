import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from PreprocessData import PreprocessData
from sklearn.model_selection import StratifiedShuffleSplit,train_test_split

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

def loadData():
    preprocessData = PreprocessData()
    df = preprocessData.readData(file="../input/train_data/train0521.csv")
    dropColumns = ['dvc_id', 'model_id']
    df = preprocessData.dropColumns(df, dropColumns)
    X = df.drop(['is_churn'],axis=1)
    y = df['is_churn']
    X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.1, random_state=42)
    return X_train,y_train, X_test,y_test

def loadTrain():
    preprocessData = PreprocessData()
    df = preprocessData.readData(file="../input/train_data/train0521.csv")
    dropColumns = ['dvc_id', 'model_id']
    df = preprocessData.dropColumns(df, dropColumns)
    X_train = df.drop(['is_churn'],axis=1)
    y_train = df['is_churn']
    return X_train,y_train

def loadTest():
    preprocessData = PreprocessData()
    df = preprocessData.readData(file="../input/test_data/test0521.csv")
    dropColumns = ['dvc_id', 'model_id']
    df = preprocessData.dropColumns(df, dropColumns)
    X_test = df.drop(['is_churn'], axis=1)
    y_test = df['is_churn']
    return X_test, y_test

def dealData(df):
    pc = PreprocessData()
    df = pc.dealUi_ver(df)
    df = pc.dealDistrict_name(df)
    df = pc.dealMain_desk(df)
    df = pc.dealPlayDays(df)

    df = pc.dealContinuousToDiscrete(df,'cv')
    df = pc.dealContinuousToDiscrete(df, 'pt')
    df = pc.dealContinuousToDiscrete(df, 'start_times')
    df = pc.dealContinuousToDiscrete(df, 'close_times')
    df = pc.dealContinuousToDiscrete(df, 'duration')
    df = pc.dealContinuousToDiscrete(df, 'desk_show_times_2s')
    df = pc.dealContinuousToDiscrete(df, 'desk_show_times_5s')
    df = pc.dealContinuousToDiscrete(df, 'desk_click_times')
    df = pc.dealContinuousToDiscrete(df, 'desk_pv')

    df = pc.dealContinuousToDiscrete(df, 'halfhour_active_days')
    df = pc.dealContinuousToDiscrete(df, 'first_start_days')
    df = pc.dealContinuousToDiscrete(df, 'eff_cv')
    df = pc.dealContinuousToDiscrete(df, 'eff_pt')

    return df

def preData(X_train,y_train,X_test,y_test):
    X_train_final, X_test_final = X_train.align(X_test, join='inner', axis=1)
    clf = RandomForestClassifier(n_estimators=500)
    #clf = XGBClassifier(learning_rate=0.01, max_depth=4,
    #                    silent=True, objective='binary:logistic')
    clf.fit(X_train_final, y_train)
    y_pred = clf.predict(X_test_final)
    return y_pred

def score(y_test,y_pred):
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import cohen_kappa_score
    from sklearn.metrics import classification_report
    print("计算模型得分 : ")
    print(confusion_matrix(y_test.as_matrix(),y_pred))

    print(classification_report(y_test.as_matrix(),y_pred))
    print("cohen_kappa得分 ",cohen_kappa_score(y_test.as_matrix(),y_pred))
    print("准确率 ",accuracy_score(y_test.as_matrix(), y_pred))
    print("召回率 ",recall_score(y_test.as_matrix(), y_pred))

def saveR(X_test,y_test,y_pred):
    result = pd.DataFrame({'is_churn_pre':y_pred.astype(np.int32)})
    result1 = pd.concat([X_test,y_test, result], axis=1)
    result1.to_csv("../output/logistic_regression_predictions1.csv", index=False)

def pltFeatureImportance(clf,X_train,y_pred):
    fig = plt.figure(figsize=(12, 6))
    feature_importance = clf.feature_importances_
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0]) + .5
    ax = fig.add_subplot(111)
    ax.barh(pos, feature_importance[sorted_idx])
    ax.set_title("Variable Importance")
    ax.set_xlabel("Relative Importance")
    ax.set_yticks(pos)
    ax.set_yticklabels(X_train.columns[sorted_idx])
    plt.tight_layout()
    plt.savefig("../output/picture/FeatureImportance")

def main():
    X_train, y_train, X_test, y_test = loadData()
    #X_train,y_train = loadTrain()
    #X_test,y_test = loadTest()

    X_train = dealData(X_train)
    X_test = dealData(X_test)

    y_pred = preData(X_train,y_train,X_test,y_test)

    saveR(X_test,y_test,y_pred)

    score(y_test, y_pred)

if __name__=="__main__":
    main()
