
# Import modules
from queries import Query
from preprocessor import tokenizeDoc, getWords
from vocabvector import Vocabvector
from heapq import heappop,heappush,heapify

def runQuery(querynumber, querytype, querylist, stopwords, index,documentbag):
    queryvector= prepareQueryVector(querynumber, querytype,querylist, stopwords, index,documentbag)
    potentialdocuments = getPotentialDocuments(Vocabvector.words,index)
    return getRankedDocuments(queryvector,potentialdocuments,Vocabvector.words,index,documentbag)


def getDocumentFrequency(token, index):
    if token in index: 
        return len(index.get(token))
    else:
        return 1 # catches the case where df = 0

#querytype: 0 = title , 1 = title + doc
def  prepareQueryVector(querynumber, querytype,querylist, stopwords, index,documentbag):
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

        tokens = tokenizeDoc(text,stopwords)
        Vocabvector.setWords(list(set(tokens)))
        queryvector = Vocabvector()

        for token in tokens:
            queryvector.setVectorValue(token, queryvector.vector[Vocabvector.words.index(token)]+1)

        for token in tokens:
            tf = queryvector.vector[Vocabvector.words.index(token)] / len(tokens)
            n = len(documentbag)
            df = getDocumentFrequency(token, index)
            queryvector.setVectorValue(token, Vocabvector.calculateTfidfWeight(tf,n,df))
        return queryvector

def getPotentialDocuments(querytokens,index):
    potentialdocuments = set()
    for token in querytokens:
        if index.get(token) != None:
            potentialdocuments.update(set(index.get(token).keys()))
    return potentialdocuments

def getDocumentvector(querytokens,index,document,documentbag):
    documentqueryvector= Vocabvector()
    for token in querytokens:
        if index.get(token) != None:
            if document in index.get(token):
                tf = index.get(token).get(document)/(len(documentbag.get(document)))
                n = len(documentbag)
                df = getDocumentFrequency(token, index)
                tfidfweight = Vocabvector.calculateTfidfWeight(tf,n,df)
                documentqueryvector.setVectorValue(token,tfidfweight)
    return documentqueryvector

def getRankedDocuments(queryvector,potentialdocuments,querytokens,index,documentbag):
    heap=[]
    heapify(heap)

    for document in potentialdocuments:
        documentvector = getDocumentvector(querytokens,index,document,documentbag)
        similairty = Vocabvector.cosineSimilarity(queryvector,documentvector)
        heappush(heap, (similairty * -1 , document))
    
    topresults = []
    for x in range(1000):
        try:
            tuple = heappop(heap)
            correctedtuple = (tuple[0]* -1, tuple[1])
            topresults.append(correctedtuple)
        except IndexError:
            break
    return topresults
        