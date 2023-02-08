from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

lTokenizer = LineTokenizer() #줄바꿈을 기준으로 리스트 생성 후 저장
print("Line tokenizer 출력 : ", lTokenizer.tokenize("My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal "
                                                  "servant to the ture emperor, Marcus Aurelius. \n Father to a murdered so, husband to a murdered wife. \n"
                                                  "And I will have my vengeance, in this life or the next."))

rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer()
print("Space Tokenizer 출력 :", sTokenizer.tokenize(rawText)) #띄어쓰기로 나누어 저장
print("Word Tokenizer 출력 : ", word_tokenize(rawText)) #띄어쓰기 + 구두점으로 구분
tTokenizer = TweetTokenizer()
print("Tweet Tokenizer 출력 : ", tTokenizer.tokenize("This is a cooool #dummysmiley: :-) :-P <3")) #해시태그나, 기호를 사용한 이모티콘을 구분
