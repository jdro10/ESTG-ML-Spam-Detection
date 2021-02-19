import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from sklearn import model_selection, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

seed = 2017

df = pd.read_csv('../datasets/no_balanced_dataset.csv')

y = df['spam']
X = df.drop(['spam'], axis=1)

rus = RandomUnderSampler()
X_RUS, y_RUS = rus.fit_sample(X, y)

sm = SMOTE()
X_SMOTE, y_SMOTE = sm.fit_sample(X, y)

print(" Positive class : ", y.tolist().count(1))
print(" Negative class : ", y.tolist().count(0))

print(" Positive class : ", y_RUS.tolist().count(1))
print(" Negative class : ", y_RUS.tolist().count(0))

print(" Positive class : ", y_SMOTE.tolist().count(1))
print(" Negative class : ", y_SMOTE.tolist().count(0))

finalUnderDf = pd.concat([X_RUS, y_RUS], axis=1)
smoteDf = pd.concat([X_SMOTE, y_SMOTE], axis=1)

smoteDf.to_csv("../datasets/balanced_dataset_smote.csv", index=False)

finalUnderDf.to_csv("../datasets/balanced_dataset_under.csv", index=False)

# invençoes

X_train, X_test, y_train, y_test = train_test_split(X_RUS, y_RUS, test_size=0.3, random_state=seed)
testTogether = pd.concat([X_test, y_test], axis=1)
testTogether.to_csv("../datasets/test_sentences_together.csv", index=False)

kfold = model_selection.StratifiedKFold(n_splits=5)
num_trees = 100

clf_rf = RandomForestClassifier(random_state=seed).fit(X_train, y_train)

rf_params = {
    "n_estimators": [100, 250, 500, 750, 1000, 2000],
    "max_depth": [1, 3, 5, 7, 9],
    'min_samples_split': [2, 3, 5],
    'min_samples_leaf': [1, 5, 8]
}

knn_params = {
    'n_neighbors': [3, 5, 11, 19],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

knn = KNeighborsClassifier().fit(X_train, y_train)

grid = GridSearchCV(clf_rf, rf_params, scoring="roc_auc", cv=kfold, verbose=10, n_jobs=10)

# grid = GridSearchCV ( knn , knn_params , scoring ="roc_auc" , cv=kfold , verbose =10, n_jobs =10)


grid.fit(X_train, y_train)

print("Best Parameters : ", grid.best_params_)

results = model_selection.cross_val_score(grid.best_estimator_, X_train,
                                          y_train, cv=kfold)

print(" Accuracy - Train CV: ", results.mean())
print(" Accuracy - Train : ", metrics.accuracy_score(grid.best_estimator_.
                                                     predict(X_train), y_train))
print(" Accuracy - Test : ", metrics.accuracy_score(grid.best_estimator_.
                                                    predict(X_test), y_test))
print(" F1 - Train : ", metrics.f1_score(grid.best_estimator_.
                                         predict(X_train), y_train))
print(" F1 - Test : ", metrics.f1_score(grid.best_estimator_.
                                        predict(X_test), y_test))
print("F1 score:  ", metrics.f1_score(grid.best_estimator_.predict(X_test), y_test))

filename = 'random_forest_model_under.sav'
joblib.dump(clf_rf, filename)
