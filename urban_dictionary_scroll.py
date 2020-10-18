import requests
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm
import time

from functions import str_to_list


def extract_total_pages(target_word):
    
    first_page_result = requests.get(f"https://www.urbandictionary.com/define.php?term={target_word}")
    first_page_soup = BeautifulSoup(first_page_result.text,"html.parser")
    pagination_centered = first_page_soup.find("div",{"class":"pagination-centered"}).find_all("a")[-1]

    last_page_url = pagination_centered.attrs['href']
    last_page_url_split = str_to_list(last_page_url)
    
    page_num_list = [int(letter) for letter in last_page_url_split if letter.isdigit()]
    last_page_num = ''.join(str(numbers) for numbers in page_num_list)
  
    return last_page_num


def extract_meanings(target_word):
    print("Initializing...")
    max_page = int(extract_total_pages(target_word))

    # if os.path.isdir("meanings") == False:
    #     os.mkdir("meanings")

    container = ""

    for a in tqdm(range(max_page), desc="Progressing...", mininterval=0.01):
        k=a+1
        if k == 1:
            page_num = k

            page_result = requests.get(f"https://www.urbandictionary.com/define.php?term={target_word}&page={page_num}")
            page_soup = BeautifulSoup(page_result.text,"html.parser")
            meanings = page_soup.find_all("div",{"class":"meaning"})
            del meanings[1]

            for i in range(len(meanings)):
                j = i+1

                extracted_text_raw = meanings[i].get_text()
                extracted_text_purified = re.sub('[^a-zA-Z0-9\n\.]', ' ', extracted_text_raw)
                extracted_text = re.sub('\.',' ', extracted_text_purified)

                container = str(container) + str("  ") + str(extracted_text)

                # f = open(f'meanings/meaning{page_num}-{j}.txt','w',encoding='utf-8')
                # f.write(extracted_text)
                # f.close()
        else:
            page_num = k

            page_result = requests.get(f"https://www.urbandictionary.com/define.php?term={target_word}&page={page_num}")
            page_soup = BeautifulSoup(page_result.text,"html.parser")
            meanings = page_soup.find_all("div",{"class":"meaning"})


            for i in range(len(meanings)):
                j = i+1

                extracted_text_raw = meanings[i].get_text()
                extracted_text_purified = re.sub('[^a-zA-Z0-9\n\.]', ' ', extracted_text_raw)
                extracted_text = re.sub('\.',' ', extracted_text_purified)

                container = str(container) + str("  ") + str(extracted_text)

                # f = open(f'meanings/meaning{page_num}-{j}.txt','w',encoding='utf-8')
                # f.write(extracted_text)
                # f.close()
        
        time.sleep(0.1)

    container = str(container)+str("\n")

    f = open('scrolled_text.txt','w',encoding='utf-8')
    f.write(container)
    f.close()

    return container

