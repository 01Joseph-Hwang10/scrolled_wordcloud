from wordcloud import WordCloud, STOPWORDS
import csv
import os

def cleaning_text(text):
    new_text = text.lower()
    new_text = ''.join([i for i in new_text if not i.isdigit()])
    new_text = new_text.strip()

    return new_text

def generate_word_cloud(text, original_word):
    print("Generating wordcloud...")
    new_text = cleaning_text(text)

    stopwords = set(STOPWORDS)
    stopwords.update(["s","d","ve","t","m","re"])

    additional_stopwords = []

    f = open('removings.csv', 'r')
    rd1 = csv.reader(f)
    for row in rd1:
        additional_stopwords.append(row[1])
    f.close()

    stopwords.update(additional_stopwords)

    wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stopwords,width=1600,height=1200)

    wc.generate(new_text)

    info_container=[]

    g = open('info.csv','r')
    rd2 = csv.reader(g)
    for row in rd2:
        info_container.append(row[1])
    g.close()

    word_hash = info_container[2]

    if os.path.isdir(f"static/image/{original_word}") == False:
        os.mkdir(f"static/image/{original_word}")

    if os.path.isfile(f"static/image/{original_word}/wordcloud_{original_word}_hash_{word_hash}.png"):
        print("Wordcloud Successfully Generated")
        return

    wc.to_file(f"static/image/{original_word}/wordcloud_{original_word}_hash_{word_hash}.png")

    print("Wordcloud Successfully Generated")




