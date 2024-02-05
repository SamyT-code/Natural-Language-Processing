import numpy as np
import math

class Vocabvector:
    words = []

    @classmethod
    def setWords(cls, list): 
        cls.words = list.copy()
    
    def __init__(self, initial_list=None):
        if initial_list is None:
            self.vector = np.array([0 for _ in range(len(Vocabvector.words))])
        else:
            self.vector = np.array(initial_list)

    def setVectorValue(self, word, value):
        try:
            self.vector[Vocabvector.words.index(word)] = value
        except ValueError:
            print("Word does not exist in VocabVector")
    
    def getMagnitude(self):
        return np.linalg.norm(self.vector)

    @classmethod
    def calculateTfidfWeight(cls, tf, n, df): 
        return tf * np.log2(n/df)
    
    @classmethod
    def cosineSimilarity(cls, vocabvector1, vocabvector2):
        return (np.dot(vocabvector1.vector, vocabvector2.vector)) / (vocabvector1.getMagnitude() * vocabvector2.getMagnitude())
