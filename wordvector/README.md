# word vector

module to make vector 01, tf, idf, tf-idf.

from nlp.sentences import Sentences

from nlp.words import Words

from wordvector.wordvector import WordVector

dlist = []

ydict = {}

with open("data.txt", "r") as file:

    data = file.read()
    
# tokenize to sentences

instsent = Sentences(data)

sent = instsent.load()

# tokenize sentences to words

for i in sent:

    tokword = Words(i)
    
    tokwordload = tokword.load()
    
    dlist.append(tokwordload)
    
# vector with tf-idf

ivect = WordVector(dlist, ngrams = 2)

vect = ivect.load()

# tf-idf of words without 0

for x, i in enumerate(vect[0]):

    for y, j in enumerate(vect[1]):
    
        if j[x] != 0:
        
            ydict[i] = j[x]
            
            break
            
listd1 = list(ydict.items())

listd1.sort(key = lambda k: k[1])

for i in listd1:

    print(i[0], "-", i[1])

requirements: nlp, wordvector from repository.
