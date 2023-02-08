from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor" \
      ", mMarcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer() #객체 초기화
pStems = [porter.stem(t) for t in tokens] # 위 tokens을 대입하는데, 뒤에 접미사를 제거하는 스테머 과정을 거친코드
#print(pStems)  #출력

lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens] #[ ~~ ] 이런식으로 대괄호 치는 이유는 연산자 우선순위 때문인듯? #PorterStemmer보다 더 많은 접미사를 제거하는 함수
print(lStems)

