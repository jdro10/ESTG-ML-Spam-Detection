import csv

num = 0

with open('../datasets/fixed_spam.csv', newline='') as old_spam_csv, open('../datasets/new_spam.csv',
                                                                          newline='') as new_spam_csv, open(
        '../datasets/new_spam_final.csv', 'w', newline='') as new_spam_final_csv:
    csvreader1 = csv.reader(old_spam_csv)
    csvreader2 = csv.reader(new_spam_csv)
    writer = csv.writer(new_spam_final_csv)

    tmp_list = []
    pos_list = []
    write_list = []
    words_list = []
    list_size = 0

    for linha in csvreader2:
        for i in range(len(linha)):
            if linha[i] != "ham" and linha[i] != "spam":
                tmp_list.append(linha[i])

    tmp_list.append("spam")
    writer.writerow(tmp_list)

    list_size = len(tmp_list)

    for linha in csvreader1:
        for i in range(len(linha)):
            for j in range(len(tmp_list)):
                if linha[i] == tmp_list[j]:
                    pos_list.append(j)
                    words_list.append(linha[i])

        write_list = [0] * list_size

        for i in range(len(pos_list)):
            for j in range(len(write_list)):
                write_list[pos_list[i]] = 1

        repeated = {i: words_list.count(i) for i in words_list}

        for i in range(len(pos_list)):
            for j in range(len(write_list)):
                write_list[pos_list[i]] = repeated[words_list[i]]

        print(repeated)

        if linha[0] == "spam":
            write_list[list_size - 1] = "true"
        else:
            write_list[list_size - 1] = "false"

        print("Loading...")
        print(num)
        num += 1
        writer.writerow(write_list)
        pos_list.clear()
        words_list.clear()
        write_list.clear()

    print("Dataset created")
