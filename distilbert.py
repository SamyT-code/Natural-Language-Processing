'''
0. turning document text and queries into dictionaries to use for encoding, storing them as json
for potenial reuse

1. encode query text using bert and save to json

2. get top 1000 results from orginal ir system 

3. encode the 1000 docs using bert (check doc word size) 

4. cosine similarity between encoded query and encodec docs 

5. print results to text file (re-use code from assigngment 1)
'''

from sentence_transformers import SentenceTransformer # pip install sentence-transformers
import multiprocessing
from multiprocessing import Process,Queue,Manager
from preprocessor import getWords
from queries import Query
from retrieval import runReRankQuery
import queue # imported for using queue.Empty exception
from index import retrieveHash, storeHash
import logging
import re
import os
from heapq import heappop,heappush
from cosine import printResults

#processes document text to return the document name and combined document text
def processDoc(rawdocumenttext):
    #creates regular expression to get all text between docno tags
    documentnumberpattern = re.compile(r"<DOCNO>(.*?)</DOCNO>")
    #finds all text fitting regular expression and puts it into a list
    documentnumber = documentnumberpattern.findall(rawdocumenttext)

    documenttextpattern = re.compile(r"<TEXT>(.*?)</TEXT>",re.DOTALL)
    documenttext = documenttextpattern.findall(rawdocumenttext)

    headlinepattern = re.compile(r"<HEAD>(.*?)</HEAD>",re.DOTALL)
    headtext = headlinepattern.findall(rawdocumenttext)

    headtext.extend(documenttext) # appends headtext list into documenttext list
    alldocumenttext = (" ".join(documenttext).replace('\n'," ")).strip()
    return (documentnumber[0].strip(), alldocumenttext)

#looks through the text of a file to process each doucment text block within the file
def processFile(filetext,documentdictionary):
    #creates regular expression to get all text between doc tags
    pattern = re.compile(r'<DOC>(.*?)</DOC>',re.DOTALL)
    #finds all text fitting regular expression and puts it into a list
    documentcontent = pattern.findall(filetext)

    #iterate through each document and 
    for document in documentcontent: 
        resultstuple = processDoc(document)
        #adds the document name and its list of stemmed tokens into a dictionary to be used in indexing
        documentdictionary.update({resultstuple[0]:resultstuple[1]})

#gets all the text with a file as one block of text
def readFile(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent

#Process each file in corpus to create a dictionarywith the doc numbers and thier text 
def processCorpus(documentdictionary): 
    #iterate through each file within folder coll
    with os.scandir('coll/') as entries: 
        count = 0
        for entry in entries:
            filetext = readFile(entry)
            processFile(filetext,documentdictionary)
            count += 1
            #print( str(count) + " file(s) done")

    return documentdictionary

#a consumer process that will encode tuple from a queue and update a dicitonary with 
#the bert encoded vector 
def encode(inqueue,dictionary):
    while True:
        try:
            #pulls from queue, doesnt need lock since order doesnt matter 
            entry = inqueue.get_nowait()
        except queue.Empty:
            #encode process stop when queue is empty
            break
        else:
            #uses pre-trained bert model to encode query text into vectors
            bertmodel = SentenceTransformer('multi-qa-distilbert-cos-v1')
            #https://www.sbert.net/docs/pretrained_models.html
            embedding = bertmodel.encode(sentences=entry[1],normalize_embeddings=True)
            dictionary.update({entry[0]: embedding.tolist()})
            print(entry[0] + " done")
    return True

#a producer proccess that intializes the queue for the consumers by 
#reading a dictionary from a json file
def embedItems(inputfilename,outputfilename):
    multiprocessing.log_to_stderr(logging.DEBUG)
    inputqueue = Queue()
    manager = Manager()
    resultsdictionary = manager.dict()

    processes = []

    data = retrieveHash(inputfilename)
    for x in data:
        inputqueue.put((x, data[x]))
    
    
    #creating processes
    for w in range(multiprocessing.cpu_count()):
        p = Process(target=encode, args=(inputqueue, resultsdictionary))
        processes.append(p)
        p.start()
    
    #wait for all sub processes to exit before continuing 
    for p in processes:
        p.join()


    storeHash(resultsdictionary.copy(), outputfilename)
    '''
    details about the numpy ndarray that were turned to list 

    Array is of type:  <class 'numpy.ndarray'>
    No. of dimensions:  2
    Shape of array:  (3, 768)
    Size of array:  2304
    Array stores elements of type:  float32
    
    '''
    return True

def getQueryVector(querynumber,mode, dictionary):
    bertmodel = SentenceTransformer('multi-qa-distilbert-cos-v1')
    querytext = ""
    match mode:
        case 0: # title 
            querytext = dictionary[querynumber].title
        case 1: # title and description 
            querytext = dictionary[querynumber].title +" "+ dictionary[querynumber].desc
    
    queryvector = bertmodel.encode(sentences=[querytext],normalize_embeddings=True)

    return queryvector

def dotProduct(vector1,vector2):
    result = 0
    for x in range(len(vector1)):
        result += vector1[x]*vector2[x]
    return result


def distilBertRerank():
    #intialize needed objects from helper directory for cosine retrieval 
    queriesdata = Query.read_queries('queries.txt')
    stopwords = getWords("stopwords.txt")
    index = retrieveHash("helper/invertedindex.json")
    maxfrequencydict = retrieveHash("helper/maxfrequency.json")

    #intialize objects for bert
    documentembeddings = retrieveHash("helper/embedbertdocuments.json")

    #change mode to 0 to query on the queries title
    #change mode to 1 to query on the queries title and description
    mode = 1

    rerankeddocs= []

    #gets the top 1000 docs from each query from the assignment 1 system 
    for query in queriesdata:
        querydocs =runReRankQuery(queriesdata[query].num, mode, queriesdata, stopwords, index,maxfrequencydict)
        queryvector = getQueryVector(query,mode, queriesdata)
        heap = []

        #calculates dot product between bert query vector and the bert encoded top 1000 relevant document vectors
        for relevantdoc in querydocs:
            documentvector= documentembeddings[relevantdoc]
            dotproduct = dotProduct(queryvector[0],documentvector)
            heappush(heap, (dotproduct * -1 , relevantdoc)) # max heap sort 

        topresults = []
        for _ in range(1000):
            try:
                tuple = heappop(heap)
                #similarity by -1 to reverse the negation when being pushed into the heap
                correctedtuple = (tuple[0]* -1, tuple[1])
                topresults.append(correctedtuple)
            except IndexError:
                break
        rerankeddocs.append(topresults)
    printResults(rerankeddocs,mode)

#main
distilBertRerank()
        
            







    



        
