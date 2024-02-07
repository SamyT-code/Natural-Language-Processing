import numpy as np
import math
import decimal

class Vocabvector:
    words = []

    @classmethod
    def setWords(cls, list): 
        cls.words = list.copy()
    
    def __init__(self):
        self.vector = np.array([0 for _ in range(len(Vocabvector.words))], dtype=float)

    def setVectorValue(self, word, value):
        try:
            self.vector[Vocabvector.words.index(word)] = value
        except ValueError:
            print("Word does not exist in VocabVector")
    
    def getMagnitude(self):
        return np.linalg.norm(self.vector)

    @classmethod
    def calculateTfidfWeight(cls, tf, n, df): 
        return decimal.Decimal(tf * np.log(n/df))
    
    @classmethod
    def cosineSimilarity(cls, vocabvector1, vocabvector2):
        return (np.dot(vocabvector1.vector, vocabvector2.vector)) / (vocabvector1.getMagnitude() * vocabvector2.getMagnitude())
