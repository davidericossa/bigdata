 
import nltk, textblob
text="""I. The Period


It was the best of times,
it was the worst of times,
it was the age of wisdom,
it was the age of foolishness,
it was the epoch of belief,
it was the epoch of incredulity,
it was the season of Light,
it was the season of Darkness,
it was the spring of hope,
it was the winter of despair,
we had everything before us,
we had nothing before us,
we were all going direct to Heaven,
we were all going direct the other way--
in short, the period was so far like the present period, that some of
its noisiest authorities insisted on its being received, for good or for
evil, in the superlative degree of comparison only.

There were a king with a large jaw and a queen with a plain face, on the
throne of England; there were a king with a large jaw and a queen with
a fair face, on the throne of France. In both countries it was clearer
than crystal to the lords of the State preserves of loaves and fishes,
that things in general were settled for ever."""

blob=textblob.TextBlob(text)
blob.words

print(nltk.pos_tag(blob.words))

lowerwords=[x.lower() for x in blob.words]

from nltk.corpus import stopwords
print(stopwords.words('english'))
filtered=list(filter(lambda x: not x in stopwords.words('english'), lowerwords))
filtered=[x for x in lowerwords if not x in stopwords.words('english')]

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
lemmas=[wnl.lemmatize(x) for x in filtered]

from nltk.corpus import wordnet as wn
list(map(lambda x :wn.synsets(x), filtered))
wn.synset('car.n.01').lemma_names()

