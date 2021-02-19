import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split

df = pd.read_csv('../datasets/balanced_dataset_under.csv')
seed = 2017

y = df['spam']
X = df.drop(['spam'], axis = 1)

X_train , X_test , y_train , y_test = train_test_split (X , y , test_size =0.3 ,random_state = seed )

loaded_model = joblib.load("RandomForest_Model.sav")
result = loaded_model.score(X_test, y_test)

print(result)

