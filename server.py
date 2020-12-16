from flask import Flask, render_template, request, redirect
import os
import csv

from main import main
from auxiliary import info_generator

app = Flask("Wordcloud Generator For UrbanDictionary")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cache_format')
def cache_format():
    return render_template("cache_format.html")

@app.route('/report',methods=['GET','POST'])
def report():
    Removings = request.args.get('Removings')
    removings_hash = request.args.get('removings_hash')
    word_for_search = request.args.get('word_for_search')

    if word_for_search:
        info_generator(word_for_search,Removings)

        container = []
        f = open('info.csv','r')
        rd = csv.reader(f)
        for row in rd:
            container.append(row[1])
        f.close()
        original_word = container[0]
        word_hash = container[2]

        container_word_history = []
        container_hash_history = []
        if os.path.isfile('search_history.csv') == False:
            f = open('search_history.csv','w')
            wr = csv.writer(f)
            wr.writerow(["number","target_word","removings_hash"])
            f.close()    
        else:
            f = open('search_history.csv','r')
            rd1 = csv.reader(f)
            for row in rd1:
                container_word_history.append(row[1])
                container_hash_history.append(row[2])
            f.close()

        if original_word in container_word_history:
            if word_hash in container_hash_history:
                return render_template("report.html", 
                         word_for_search=word_for_search, Removings=Removings, removings_hash=removings_hash)

        word_for_search = word_for_search.lower()
        main(word_for_search,Removings)

        info_container=[]
        g = open('info.csv','r')
        rd2 = csv.reader(g)
        for row in rd2:
            info_container.append(row[1])
        g.close()
        searched_word = info_container[0]
        removings_hash = info_container[2]

        f = open('search_history.csv','r')
        rd3 = csv.reader(f)
        i=-1
        for row in rd3:
            i = i+1
        f.close()

        f = open('search_history.csv','a',newline='\n')
        wr = csv.writer(f)
        wr.writerow([int(i),str(searched_word),str(removings_hash)])
        f.close()
    else:
        return redirect('/')

    return render_template("report.html", 
    word_for_search=word_for_search, Removings=Removings, removings_hash=removings_hash)

app.run()