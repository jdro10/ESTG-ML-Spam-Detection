import re
import csv
import unidecode
import wordninja as wn
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# if first time run this code
# import nltk
# nltk.download

wordnet_lemmatizer = WordNetLemmatizer()

fixed_spell_list = []
spell = SpellChecker()
stopwords = set(stopwords.words('english'))


def remove_duplicates(l):
    return list(set(l))


def ler():
    tuples = []

    with open("../datasets/spam.csv") as fp:
        for linha in fp:
            linha = linha.strip().split(",")
            s = str(linha[1:-3])
            s = re.sub(r'[^\w\s]', '', s)

            word_tokens = word_tokenize(s)
            filtered_sentence = [w for w in word_tokens if not w in stopwords]

            for w in word_tokens:
                if w not in stopwords:
                    unaccented_w = unidecode.unidecode(str(w))
                    filtered_sentence.append(unaccented_w)

            tuples += remove_duplicates(filtered_sentence)

    fp.close()

    for i in range(len(tuples)):
        tuples[i] = tuples[i].lower()

    tuples = remove_duplicates(tuples)

    return tuples


removed_duplicates_list = ler()
list_size = len(removed_duplicates_list)

for i in range(list_size):
    fixed_spell = spell.correction(removed_duplicates_list[i])
    fixed_spell_list.append(fixed_spell)

    percentage = (i / list_size) * 100

    print(str(round(percentage, 2)) + "%")

remove_duplicates_after_spell_check = remove_duplicates(fixed_spell_list)

remove_duplicates_after_spell_check.append("spam")

new_list_tmp = []

for i in range(len(remove_duplicates_after_spell_check)):
    word = wn.split(remove_duplicates_after_spell_check[i])
    for j in range(len(word)):
        if word[j].isnumeric():
            pass
        else:
            new_list_tmp.append(word[j])

remove_duplicates_again = remove_duplicates(new_list_tmp)

final_list = []
final_remove_duplicates = []

for i in range(len(remove_duplicates_again)):
    palavra = wordnet_lemmatizer.lemmatize(remove_duplicates_again[i], pos="v")
    final_list.append(palavra)


final_remove_duplicates = remove_duplicates(final_list)

with open('../datasets/new_spam.csv', 'w', newline='') as new_csvfile:
    csvreader1 = csv.writer(new_csvfile)
    csvreader1.writerow(final_remove_duplicates)
    print("New dataset created")
