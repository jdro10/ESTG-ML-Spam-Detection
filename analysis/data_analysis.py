import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

smote_dataset = pd.read_csv('../datasets/balanced_dataset_smote.csv')
under_dataset = pd.read_csv('../datasets/balanced_dataset_under.csv')

sum_smote = smote_dataset.sum()
dict_words = dict(sum_smote)

sum_under = under_dataset.sum()
dict_words_under = dict(sum_under)

sorted_x = dict(sorted(dict_words.items(), key=lambda item: item[1]))
sorted_x_under = dict(sorted(dict_words_under.items(), key=lambda item: item[1]))

dict_smote = {}
dict_under = {}

i = 0
j = 0

for key, value in sorted_x.items():
    if key != "spam" and i >= len(sorted_x) - 11 and len(key) > 1:
        dict_smote[key] = value

    i += 1

for key, value in sorted_x_under.items():
    if key != "spam" and j >= len(sorted_x_under) - 11 and len(key) > 1:
        dict_under[key] = value

    j += 1

dict_sum_smote = {}
dict_sum_under = {}
dict_sum_original_dataset = {}

reader_smote = pd.read_csv('../datasets/balanced_dataset_smote.csv')
reader_under = pd.read_csv('../datasets/balanced_dataset_under.csv')
reader_original_dataset = pd.read_csv('../datasets/spam.csv', encoding='latin-1')

count_ham_smote, count_spam_smote = reader_smote['spam'].value_counts()
dict_sum_smote["spam"] = count_spam_smote
dict_sum_smote["ham"] = count_ham_smote

count_ham_under, count_spam_under = reader_under['spam'].value_counts()
dict_sum_under["spam"] = count_spam_under
dict_sum_under["ham"] = count_ham_under

count_ham_original_dataset, count_spam_original_dataset = reader_original_dataset['v1'].value_counts()
dict_sum_original_dataset["spam"] = count_spam_original_dataset
dict_sum_original_dataset["ham"] = count_ham_original_dataset

fixed_original_spam = pd.read_csv('../datasets/new_spam_final.csv')
sum_fixed_original_spam = fixed_original_spam.sum()
sorted_fixed_original_spam = dict(sorted(dict_words.items(), key=lambda item: item[1]))

dict_fixed_original_spam = {}

k = 0

for key, value in sorted_fixed_original_spam.items():
    if key != "spam" and k >= len(sorted_fixed_original_spam) - 11 and len(key) > 1:
        dict_fixed_original_spam[key] = value

    k += 1

sns.barplot(x=list(dict_fixed_original_spam.keys()), y=list(dict_fixed_original_spam.values()))
plt.title('Top 10 most frequent words original dataset')
plt.xlabel('Word', fontsize=18)
plt.ylabel('Number of words', fontsize=16)
plt.savefig('../img/top10_words_original_dataset.png')
plt.show()

sns.barplot(x=list(dict_sum_original_dataset.keys()), y=list(dict_sum_original_dataset.values()))
plt.title('Number of spam and ham SMS in original dataset')
plt.xlabel('Spam or Ham SMS', fontsize=18)
plt.ylabel('Number of SMS', fontsize=16)
plt.savefig('../img/number_of_spam_and_ham_sms_original_dataset.png')
plt.show()

sns.barplot(x=list(dict_sum_under.keys()), y=list(dict_sum_under.values()))
plt.title('Number of spam and ham SMS using UnderSampling')
plt.xlabel('Spam or Ham SMS', fontsize=18)
plt.ylabel('Number of SMS', fontsize=16)
plt.savefig('../img/number_of_spam_and_ham_sms_UnderSampling.png')
plt.show()

sns.barplot(x=list(dict_sum_smote.keys()), y=list(dict_sum_smote.values()))
plt.title('Number of spam and ham SMS using SMOTE')
plt.xlabel('Spam or Ham SMS', fontsize=18)
plt.ylabel('Number of SMS', fontsize=16)
plt.savefig('../img/number_of_spam_and_ham_sms_SMOTE.png')
plt.show()

sns.barplot(x=list(dict_smote.keys()), y=list(dict_smote.values()))
plt.title('Top 10 most frequent words SMOTE dataset')
plt.xlabel('Word', fontsize=18)
plt.ylabel('Number of words', fontsize=16)
plt.savefig('../img/top10_words_smote.png')
plt.show()

sns.barplot(x=list(dict_under.keys()), y=list(dict_under.values()))
plt.title('Top 10 most frequent words UNDER dataset')
plt.xlabel('Word', fontsize=18)
plt.ylabel('Number of words', fontsize=16)
plt.savefig('../img/top10_words_under.png')
plt.show()
