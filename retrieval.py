
# Import modules
from index import retrieveHash
from queries import Query
from preprocessor import removeUnwanted, stemTokens, getWords
from heapq import heappop,heappush,heapify
from collections import Counter
import math

def runQuery(querynumber, querytype, querylist, stopwords, index,maxfrequencydict):
    queryvector, querytokens= prepareQueryVector(querynumber, querytype,querylist, stopwords, index)
    potentialdocuments = getPotentialDocuments(querytokens,index)
    topresults = getRankedDocuments(queryvector,potentialdocuments,querytokens,index,maxfrequencydict)
    return topresults

def getDocumentFrequency(token, index):
    if token in index: 
        return (len(index.get(token)))
    else:
        return 0 # catches the case where df = 0


def getInvertedDocumentFrequency(token,index): 
    
    if getDocumentFrequency(token,index) == 0:
        return 0
    else:
        return math.log2(79923/(getDocumentFrequency(token,index)))

def makeQueryVector(tokens,index):
    organizedtokens = Counter(tokens)
    maxfrequency = organizedtokens.most_common(1)[0][1]

    
    for token in organizedtokens:
        tf = organizedtokens[token]/maxfrequency
        idf =getInvertedDocumentFrequency(token,index)
        organizedtokens[token] = tf*idf
    
    return organizedtokens

def makeDocumentVector(tokens,document,index,maxfrequencydict):
    organizedtokens = {}
    maxfrequency = maxfrequencydict.get(document)

    for token in tokens:
        tf = 0
        if index.get(token) != None:
            if index.get(token).get(document) != None:
                tf = index.get(token).get(document) / maxfrequency
        idf =getInvertedDocumentFrequency(token,index)
        organizedtokens[token] = tf * idf
    
    return organizedtokens

def dotProduct(vector1, vector2, tokens):
    sum = 0
    for token in tokens:
        sum += (vector1.get(token) * vector2.get(token))
    return sum

def vectorMagnitude(vector):
    sum = 0
    for entries in vector:
        sum += (vector.get(entries) ** 2)
    return math.sqrt(sum)

#querytype: 0 = title , 1 = title + doc
def  prepareQueryVector(querynumber, querytype,querylist, stopwords, index,):
    query = querylist.get(querynumber)
    if query == None:
        print("Query number does not exist")
        exit()
    else:
        text = ""
        match querytype:
            case 0:
                text = query.title
            case 1:
                text = query.title + " " + query.desc
            case _:
                print("Invalid querytype")

        unstemmedquerytokens = removeUnwanted(text, stopwords)
        stemmedquerytokens = stemTokens(unstemmedquerytokens)

        querysettokens = list(set(stemmedquerytokens))

        queryvector = makeQueryVector(stemmedquerytokens,index)
        
        return queryvector, querysettokens

def getPotentialDocuments(querytokens,index):
    potentialdocuments = set()
    for token in querytokens:
        if index.get(token) != None:
            potentialdocuments.update(set(index.get(token).keys()))
    return potentialdocuments

def getCosineSimilarity(vector1,vector2,tokens):
    numerator = dotProduct(vector1,vector2,tokens)
    denominator = vectorMagnitude(vector1) * vectorMagnitude(vector2)

    return numerator / denominator

def getRankedDocuments(queryvector,potentialdocuments,querytokens,index,maxfrequencydict):
    heap=[]
    docvectors = {}
    for document in potentialdocuments:
        documentvector = makeDocumentVector(querytokens,document,index,maxfrequencydict)
        docvectors.update({document: documentvector})
        similairty = getCosineSimilarity(queryvector,documentvector,querytokens)
        heappush(heap, (similairty * -1 , document))
    
    topresults = []
    for _ in range(1000):
        try:
            tuple = heappop(heap)
            correctedtuple = (tuple[0]* -1, tuple[1])
            topresults.append(correctedtuple)
        except IndexError:
            break
    return topresults
    #return topresults,querytokens,queryvector, docvectors


#main

'''
queries_data = Query.read_queries("testing_files/queries.txt")
stopwords=getWords("testing_files/stopwords.txt")
index = retrieveHash("testing_files/invertedindex3.json")
maxfrequencydict = retrieveHash("testing_files/maxfrequency.json")

prepareQueryVector(50,0,queries_data,stopwords,index)
'''




        