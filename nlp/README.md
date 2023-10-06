# nlp

tokenize to sentences, words, stop-words, stemming (ru)

from nlp.tokenize import Tokenize
from nlp.stem import Stemming
from nlp.corpus import Corpus
with open("testdata.txt", "r") as file:
    text = file.read()
# tokenize to words
tokword = Tokenize(text)
tokwordload = tokword.words()
print("\nword tokenize:\n", tokwordload)
# load stop words
stop = Corpus()
stopw = stop.stopwords("ru")
stopfiltered = [x for x in tokwordload if x not in stop]
print("\nwithout stop words:\n", stopfiltered)
# load stemming form
st = corpus.stemming()
# stemming text
stemming = Stemming(*st)
stem = stemming.load(stopfiltered)
print("\nto stemming:\n", stem)
