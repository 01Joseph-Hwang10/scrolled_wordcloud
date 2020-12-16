# pip3.8 path : C:\Users\josep\AppData\Local\Programs\Python\Python38-32\Scripts\pip3.8

from urban_dictionary_scroll import extract_meanings
from word_cloud import generate_word_cloud


def main(word_for_search,removings):
    scrolled_text = extract_meanings(word_for_search)
    generate_word_cloud(scrolled_text[0],scrolled_text[1])
