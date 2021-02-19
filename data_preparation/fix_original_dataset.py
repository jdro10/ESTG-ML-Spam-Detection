import re
import csv
import wordninja as wn
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

stopwords = set(stopwords.words('english'))


def remove_duplicates(l):
    return list(set(l))


i = 0

with open('../datasets/spam.csv', newline='') as new_csvfile, open('../datasets/fixed_spam.csv', 'w',
                                                                   newline='') as new_fixed_csvfile:
    writer = csv.writer(new_fixed_csvfile)
    tuples = []

    for linha in new_csvfile:
        linha = linha.strip().split(",")
        s = str(linha[1:-3])
        s = re.sub(r'[^\w\s]', '', s)
        spam = False

        if linha[0] == "spam":
            spam = True

        word_tokens = word_tokenize(s)
        filtered_sentence = [w for w in word_tokens if not w in stopwords]

        for w in word_tokens:
            if w not in stopwords:
                unaccented_w = unidecode.unidecode(str(w))
                filtered_sentence.append(unaccented_w)

        tuples = remove_duplicates(filtered_sentence)

        tmp_list = []
        new_tmp_list = []
        list_to_write = []

        for i in range(len(tuples)):
            tmp_list.append(tuples[i].lower())
            palavra = wordnet_lemmatizer.lemmatize(tmp_list[i], pos="v")

            word = wn.split(palavra)
            for j in range(len(word)):
                if word[j].isnumeric():
                    pass
                else:
                    new_tmp_list.append(word[j])

        list_to_write = remove_duplicates(new_tmp_list)

        if spam:
            list_to_write.insert(0, "spam")
        else:
            list_to_write.insert(0, "ham")

        if i != 0 and list_to_write:
            writer.writerow(list_to_write)

        i += 1

    print("Fixed spam dataset created")
