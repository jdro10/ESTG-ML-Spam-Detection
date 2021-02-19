import pandas as pd

df = pd.read_csv('../datasets/Balanced_Dataset_Smote.csv')

df = df.loc[df['spam'] == True]

df = df.drop(["spam"], axis=1)

df.to_csv("../datasets/only_spam_dataset_smote.csv", index=False)

print(df)

##correr este 1º