import json
from wordvector.wordvector import WordVector
from wordvector.fit import Fit
from wordvector.cossim import CosSim
from nlp.tokenize import Tokenize

cold = 0
history = []
historyind = []
dlist = []

with open("data.json", "r") as file:
    data = json.load(file)

for i in data:
    w = Tokenize(i)
    wl = w.words()
    dlist.append(wl)

# vector with tf-idf
ivect = WordVector(dlist)
vect = ivect.load()
f = Fit(dlist, vect)
fr = f.fit()
while True:
    tlist = []
    wlist = []
    result = []
    if cold == 0: 
        print("Recomendation movie: ", data[0])
        history.append(dlist[0])
        historyind.append(0)
        inp = input("continue?(y/n) ")
        if inp == "y":
            cold = 1
        else:
            exit()
    else:
        if len(history) == 1:
            for i in history:
                for j in i:
                    wlist.append(1)
        else:
            ivect2 = WordVector(history)
            vect2 = ivect2.load()
            f2 = Fit(history, vect2)
            fr2 = f2.fit()
            for i in fr2:
                for j in i:
                    wlist.append(j)
        for i in history:
            for j in i:
                tlist.append(j)
        for y, i in enumerate(dlist):
            tmplist = []
            for j in tlist:
                for x, k in enumerate(i):
                    if k == j:
                        tmplist.append(fr[y][x])
            c = CosSim(wlist, tmplist)
            cw = c.cossim()
            result.append((y, cw))
        result.sort(key = lambda x: x[1])
        for i in reversed(result):
            if i[0] not in historyind:
                history.append(dlist[i[0]])
                historyind.append(i[0])
                print("Recomendation movie: ", data[i[0]])
                if len(historyind) != len(dlist):
                    inp2 = input("continue?(y/n) ")
                    if inp2 == "y":
                        break
                else:
                    print("Recomendation end")
                    exit()
