
#need to install nltk for this assignment 
import os
import string
from nltk.stem import PorterStemmer
import re

#initializes a set by reading a text file line by line
def getWords(filename): 
    file = open(filename,'r')
    words = set()
    while True: 
        line=file.readline()
        if not line:
            break
        words.add(line.strip())
    return words

#gets all the text with a file as one block of text
def readFile(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent

#removes punctuation, digits and words found within stop words parameter
def removeUnwanted(text,stopwords):
    numberless = re.sub(r'\d+', '', text) #removes all digits in text with ''
    lowercase = numberless.lower()
    hyphensplit = lowercase.replace("'", "")
    #replaces  all punctuation with a " "
    nopunctuation = hyphensplit.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    rawtokens = nopunctuation.split()
    
    nonstemmedtokens = []
    for word in rawtokens:
        if word in stopwords or not word.isalpha(): 
            continue
        else:
            nonstemmedtokens.append(word)
        
    return nonstemmedtokens

#will stem the each word in list tokens and returns a list of the stemmed words
def stemTokens(tokens):
    porter = PorterStemmer()
    stemmedtokens = []

    for word in tokens:
        stemmedtokens.append(porter.stem(word))
    
    return stemmedtokens

#processes document text to return the document name and its stemmed tokens
def processDoc(rawdocumenttext,stopwords):
    #creates regular expression to get all text between docno tags
    documentnumberpattern = re.compile(r"<DOCNO>(.*?)</DOCNO>")
    #finds all text fitting regular expression and puts it into a list
    documentnumber = documentnumberpattern.findall(rawdocumenttext)

    documenttextpattern = re.compile(r"<TEXT>(.*?)</TEXT>",re.DOTALL)
    documenttext = documenttextpattern.findall(rawdocumenttext)

    headlinepattern = re.compile(r"<HEAD>(.*?)</HEAD>",re.DOTALL)
    headtext = headlinepattern.findall(rawdocumenttext)

    documenttext.extend(headtext) # appends headtext list into documenttext list
    unstemmedtokens = removeUnwanted(" ".join(documenttext),stopwords)

    stemmedtokens = stemTokens(unstemmedtokens)

    tokenset = stemmedtokens.copy() 

    return (documentnumber[0].strip(), stemmedtokens, tokenset)

#looks through the text of a file to process each doucment text block within the file
def processFile(filetext,documentdictionary,vocabset,stopwords):
    #creates regular expression to get all text between doc tags
    pattern = re.compile(r'<DOC>(.*?)</DOC>',re.DOTALL)
    #finds all text fitting regular expression and puts it into a list
    documentcontent = pattern.findall(filetext)

    #iterate through each document and 
    for document in documentcontent: 
        resultstuple = processDoc(document,stopwords)
        #adds the document name and its list of stemmed tokens into a dictionary to be used in indexing
        documentdictionary.update({resultstuple[0]:resultstuple[1]})
        #add the stemmed tokens of document into the set of unique tokens of the entire corpus
        vocabset.update(resultstuple[2])
    
#Process each file in corpus to create the vocabulary and a dictionary of all the stemmed tokens of each document
def processCorpus(documentdictionary,vocabset,stopwords): 
    #iterate through each file within folder coll
    with os.scandir('coll/') as entries: 
        for entry in entries:
            filetext = readFile(entry)
            processFile(filetext,documentdictionary,vocabset,stopwords)
    return vocabset,documentdictionary
        




#main 


