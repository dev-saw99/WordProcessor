import nltk
import json
from nltk.corpus import brown

genres = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance',
'science_fiction']
dictionary = {}
for genre in genres:
    dic = brown.words(categories=genre)
    dictionary = {**dictionary,**nltk.FreqDist(wrd.lower() for wrd in dic)}
    
with open('dictionary.txt','w') as output:
    json.dump(dictionary,output)

            


