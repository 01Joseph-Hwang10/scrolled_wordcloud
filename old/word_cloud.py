from wordcloud import WordCloud, STOPWORDS
import csv

def cleaning_text(text):
    new_text = text.lower()
    new_text = ''.join([i for i in new_text if not i.isdigit()])
    new_text = new_text.strip()

    return new_text

def generate_word_cloud(text):
    print("Generating wordcloud...")
    new_text = cleaning_text(text)

    stopwords = set(STOPWORDS)
    stopwords.update(["s","d","ve","t","m","re"])

    additional_stopwords = []

    f = open('removings.csv', 'r')
    rd = csv.reader(f)
    for row in rd:
        additional_stopwords.append(row[1])
    f.close()

    stopwords.update(additional_stopwords)

    wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stopwords,width=1600,height=1200)

    wc.generate(new_text)
    wc.to_file("templates/wordcloud.png")

    print("Wordcloud Successfully Generated")




