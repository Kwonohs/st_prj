import nltk
from nltk.corpus import gutenberg
#print(gutenberg.fileids())

gb_words = gutenberg.words('bible-kjv.txt') #gb_words 변수에 bible-kjv의 모든 단어 목록 저장
words_filtered = [e for e in gb_words if len(e) >= 3] #bible-kjv 단어들 중 2글자 이하를 제외한 단어를 words_filtered에 저장
#print(words_filtered)

stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]

fdistPlain = nltk.FreqDist(words)
fdist = nltk.FreqDist(gb_words)

print("Following are the most common 10 words in the bag")
print(fdist.most_common(10))
print("Following are the most common 10 words in the bag minus the stopwords")
print(fdistPlain.most_common(10))