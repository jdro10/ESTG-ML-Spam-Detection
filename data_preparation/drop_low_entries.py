import pandas as pd

df = pd.read_csv("../datasets/balanced_dataset_smote.csv")

for column in df.columns:
    word = str(column)
    if word.__contains__("sex"):
        df['sex'] = df.loc[:, ['sex', word]].sum(axis=1)
    if len(word) < 3:
        df.drop(column, axis=1, inplace=True)
    if word == "www":  # coluna importante para verificar a existencia de spam mas não tanto para o caracterizar
        df.drop(column, axis=1, inplace=True)

for column in df.columns:
    if df[column].sum() < 15:
        df.drop(column, axis=1, inplace=True)

df.to_csv("../datasets/drop_low_entries_dataset_smote.csv", index=False)

# correr o que esta comentado
