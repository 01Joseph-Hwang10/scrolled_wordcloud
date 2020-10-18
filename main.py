# pip3.8 path : C:\Users\josep\AppData\Local\Programs\Python\Python38-32\Scripts\pip3.8

import csv

from urban_dictionary_scroll import extract_meanings
from word_cloud import generate_word_cloud

word_for_search = "asshole"

f = open('removings.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "asshole"])
wr.writerow([2,"assholes"])
f.close()

def main():
    scrolled_text = extract_meanings(word_for_search)
    generate_word_cloud(scrolled_text)

main()
