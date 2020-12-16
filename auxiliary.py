import os
import hashlib
import re
import csv

# subordinate functions

def str_to_list(word):
    return [char for char in word]

def info_generator(target_word,words):
    words == words.lower()
    

    if len(words)==0:
        f = open('info.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(["target_word",target_word])
        wr.writerow(["removings_name","None"])
        wr.writerow(["hash","None"])
        f.close()

        g = open('removings.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(g)
        wr.writerow(["removings",":("])
        return

    words_text_purified = re.sub('[^a-zA-Z0-9\n\.]', ' ', words)
    words_text = re.sub('\.',' ', words_text_purified)
    removings = words_text.split()
    removings.sort()
    removings_name = ''

    if len(removings)==0:
        f = open('info.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(["target_word",target_word])
        wr.writerow(["removings_name","None"])
        wr.writerow(["hash","None"])
        f.close()

        g = open('removings.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(g)
        wr.writerow(["removings",":("])
        return

        
    i = 0
    for words in removings:
        removings_name = str(removings_name) + str(removings[i]) + str(" ")
        i = i+1

    f = open('info.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(["target_word",target_word])
    wr.writerow(["removings_name",removings_name])
    wr.writerow(["hash",hashlib.md5(str(removings_name).encode('utf-8')).hexdigest()])
    f.close()
    
    g = open('removings.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(g)
    i = 1
    for removings in removings:
        wr.writerow([i,removings])
        i = i+1
    g.close()

