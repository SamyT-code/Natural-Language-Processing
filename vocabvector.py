
import numpy as np
import math

'''
remeber to add to read me how to install numpy 
'''
class Vocabvector: 
    words = []

    @classmethod
    def setWords(cls,list): # this should always be set before making a VocabVector.
        cls.words = list.copy()
    
    def __init__(self):
        if len(Vocabvector.words) != 0:
            self.vector = np.array([0 for i in range(len(Vocabvector.words))])
        else:
            self.vector = np.array([])
    
    def __init__(self,list):
        self.vector = np.array(list)

    def setVectorValue(self,word,value):
        try:
            self.vector[Vocabvector.words.index(word)] = value
        except ValueError:
            print("Word does not exist in VocabVector")
    
    def getMaginitude(self):
        return np.linalg.norm(self.vector)

    @classmethod
    def calculateTfidfWeight(cls,tf, n, df): # tf = term frequency, n = total number of documents and df = document frequency
        return tf * np.log2(n/df)
    
    @classmethod
    def cosineSimilarity(cls,vocabvector1, vocabvector2):
        return (np.dot(vocabvector1.vector,vocabvector2.vector))/ (vocabvector1.getMaginitude() * vocabvector2.getMaginitude())

