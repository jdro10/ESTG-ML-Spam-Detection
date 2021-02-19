import joblib
import csv
import numpy as np
import wordninja as wn
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import unidecode

stopwords = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()


def remove_duplicates(l):
    return list(set(l))


def index_test():
    return "Index test"


def spam_or_not_spam(string):
    st = string.split(" ")
    list_string = list(st)
    tmp_list = []
    new_tmp_list = []

    s = str(list_string)
    s = re.sub(r'[^\w\s]', '', s)

    word_tokens = word_tokenize(s)

    filtered_sentence = [w for w in word_tokens if not w in stopwords]

    for w in word_tokens:
        if w not in stopwords:
            unaccented_w = unidecode.unidecode(str(w))
            filtered_sentence.append(unaccented_w)

    for i in range(len(filtered_sentence)):
        tmp_list.append(filtered_sentence[i].lower())
        word = wordnet_lemmatizer.lemmatize(tmp_list[i], pos="v")
        wordd = wn.split(word)

        for j in range(len(wordd)):
            if wordd[j].isnumeric():
                pass
            else:
                new_tmp_list.append(wordd[j])

    remove_duplicates_list = remove_duplicates(new_tmp_list)

    first_row = []
    write_list = []
    pos_list = []
    words_list = []

    with open("../../datasets/balanced_dataset_under.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            first_row = row
            break

    for i in range(len(first_row)):
        for j in range(len(new_tmp_list)):
            if first_row[i] == new_tmp_list[j]:
                pos_list.append(i)
                words_list.append(first_row[i])

    write_list = [0] * (len(first_row) - 1)

    for i in range(len(pos_list)):
        for j in range(len(write_list)):
            write_list[pos_list[i]] = 1

    repeated = {i: words_list.count(i) for i in words_list}

    for i in range(len(pos_list)):
        for j in range(len(write_list)):
            write_list[pos_list[i]] = repeated[words_list[i]]

    loaded_model = joblib.load("../../modeling_and_evaluation/saved_models/RandomForest_Model_Under.sav")

    write_list = np.array([write_list])
    result = loaded_model.predict(write_list)

    res = str(result)

    if res == "[False]":
        var_to_return = "ham"
    else:
        var_to_return = "spam"

    ret = {
        "spam": var_to_return
    }

    return ret
