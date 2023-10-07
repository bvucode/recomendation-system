import json
from wordvector.wordvector import WordVector
from wordvector.fit import Fit
from wordvector.cossim import CosSim
from nlp.tokenize import Tokenize

cold = 0
history = []
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
    tlist2 = []
    wlist = []
    result = []
    if cold == 0: 
        print("Recomendation movie: ", data[0])
        history.append(0)
        inp = input("continue?(y/n) ")
        if inp == "y":
            cold = 1
        else:
            exit()
    else:
        if len(history) == 1:
            for i in history:
                for j in dlist[i]:
                    wlist.append(1)
        else:
            for i in history:
                tlist.append(dlist[i])
            ivect2 = WordVector(tlist)
            vect2 = ivect2.load()
            f2 = Fit(tlist, vect2)
            fr2 = f2.fit()
            for i in fr2:
                for j in i:
                    wlist.append(j)
        for i in history:
            for j in dlist[i]:
                tlist2.append(j)
        for y, i in enumerate(dlist):
            tmplist = []
            for j in tlist2:
                for x, k in enumerate(i):
                    if k == j:
                        tmplist.append(fr[y][x])
            c = CosSim(wlist, tmplist)
            cw = c.cossim()
            result.append((y, cw))
        result.sort(key = lambda x: x[1])
        for i in reversed(result):
            if i[0] not in history:
                history.append(i[0])
                print("Recomendation movie: ", data[i[0]])
                if len(history) != len(dlist):
                    inp2 = input("continue?(y/n) ")
                    if inp2 == "y":
                        break
                else:
                    print("Recomendation end")
                    exit()
