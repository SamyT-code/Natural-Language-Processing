
# Import modules
from preprocessor import removeUnwanted, stemTokens, getWords
from heapq import heappop,heappush,heapify
from collections import Counter
import math

#returns a list  top 1000 results of a query 
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
    #we add 1 to document frequency to avoid dividing by zero 
    return math.log2(79923/((getDocumentFrequency(token,index))+1))

#returns a dictionary with token and its tf-idf weight representing the query vector
def makeQueryVector(tokens,index):
    organizedtokens = Counter(tokens)
    maxfrequency = organizedtokens.most_common(1)[0][1]

    for token in organizedtokens:
        #double normalization of term frequency
        tf = 0.5+ (0.5 *(organizedtokens[token])/maxfrequency)
        idf =getInvertedDocumentFrequency(token,index)
        organizedtokens[token] = tf*idf
    
    return organizedtokens

def makeDocumentVector(tokens,document,index,maxfrequencydict):
    organizedtokens = {}
    maxfrequency = maxfrequencydict.get(document)

    for token in tokens:
        tf = 0

        #check if tokens of query is in the index
        if index.get(token) != None:
            #check if the document contains the token of query 
            if index.get(token).get(document) != None:
                 #double normalization of term frequency
                tf = 0.5 + (0.5 * (index.get(token).get(document))/ maxfrequency)
        idf =getInvertedDocumentFrequency(token,index)
        organizedtokens[token] = tf * idf
    
    return organizedtokens

#vector1 and vector2 are dictionaries that represent query and document vector
def dotProduct(vector1, vector2, tokens):
    sum = 0
    for token in tokens:
        sum += (vector1.get(token) * vector2.get(token))
    return sum

#Vector is a dictionary representing a vector
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

        #processing and stemming the text in query 
        unstemmedquerytokens = removeUnwanted(text, stopwords)
        stemmedquerytokens = stemTokens(unstemmedquerytokens)

        #set of tokens in query (removing repeats)
        querysettokens = list(set(stemmedquerytokens))

        queryvector = makeQueryVector(stemmedquerytokens,index)
        
        return queryvector, querysettokens

#given a list of tokens of the query
#returns all the documents name that contain at least one token within the list of tokens
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
    #use a max heap to sort the cosine similarty
    heap=[]
    for document in potentialdocuments:
        documentvector = makeDocumentVector(querytokens,document,index,maxfrequencydict)
        similairty = getCosineSimilarity(queryvector,documentvector,querytokens)
        #multiply similarity by -1 as heapq implements a min heap 
        heappush(heap, (similairty * -1 , document))
    
    topresults = []
    for _ in range(1000):
        try:
            tuple = heappop(heap)
            #similarity by -1 to reverse the negation when being pushed into the heap
            correctedtuple = (tuple[0]* -1, tuple[1])
            topresults.append(correctedtuple)
        except IndexError:
            break
    return topresults


#main

'''
queries_data = Query.read_queries("testing_files/queries.txt")
stopwords=getWords("testing_files/stopwords.txt")
index = retrieveHash("testing_files/invertedindex3.json")
maxfrequencydict = retrieveHash("testing_files/maxfrequency.json")

prepareQueryVector(50,0,queries_data,stopwords,index)
'''




        