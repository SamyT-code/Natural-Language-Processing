from vocabvector import Vocabvector

#Vocabvector.setWords(["hi","hello","bye"])

v1 = Vocabvector([0,0,2])
v2 = Vocabvector([2,3,5])


print(Vocabvector.cosineSimilarity(v1,v2))