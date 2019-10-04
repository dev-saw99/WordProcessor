import json
import re
import nltk

try:
    dictionary_data = open('dictionary.txt','r')
except OSError:
    print('!MISSING_DICTONARY , Run dictionary.py as python script.')

dictionary = json.load(dictionary_data)

class spellcheck():
    
    def get_words(self,line):
        
        # extract english words from the string

        return  re.findall(r'[a-zA-Z_\']+',line)

    def Scheck(self,line):
        correct_suggestion = []
        self.words = [wrd.lower() for wrd in self.get_words(line)]
        dist=0
        for word in self.words:
            if word in dictionary:
                continue
            else:
                dist=999
                for correct_words in dictionary:
                    cur_dist = nltk.edit_distance(word,correct_words)
                    if(cur_dist<dist):
                        suggestion = correct_words
                        dist = cur_dist

                correct_suggestion.append(suggestion)
        return correct_suggestion    

    
sp = spellcheck()
print(sp.Scheck('hello! this is awesowm prograem good qord is evrything you expect from the dictionay nothing can go well in te gaem ehre its hard to plya with pponnet'))
