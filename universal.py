
from index import retrieveHash, storeHash
from queries import Query
from heapq import heappop,heappush
from retrieval import runReRankQuery
from cosine import printResults
from preprocessor import getWords

def getQueryVector(querynumber,mode, dictionary):
    queryvector=[]
    match mode:
        case 0: # title 
            queryvector = dictionary[str(querynumber)][0][0]
        case 1: # title and description 
            queryvector = dictionary[str(querynumber)][2][0]
    
    return queryvector

def dotProduct(vector1,vector2):
    #compute similarity between vectors
    result = 0
    for x in range(len(vector1)):
        result += vector1[x]*vector2[x]
    return result


def universalReRank():
    #intialize needed objects from helper directory for cosine retrieval 
    queriesdata = Query.read_queries('queries.txt')
    stopwords = getWords("stopwords.txt")
    index = retrieveHash("helper/invertedindex.json")
    maxfrequencydict = retrieveHash("helper/maxfrequency.json")

    querydict = retrieveHash("helper/universalqueries.json")
    '''
    querydict is a 3d array so to get the vector you would need to do something like 
    querydict["1"][0][0]
    '''
    documentembeddings = retrieveHash("helper/universaldocuments.json")

    #change mode to 0 to query on the queries title
    #change mode to 1 to query on the queries title and description
    mode = 1

    rerankeddocs= []

    #gets the top 1000 docs from each query from the assignment 1 system 
    for query in queriesdata:
        querydocs =runReRankQuery(queriesdata[query].num, mode, queriesdata, stopwords, index,maxfrequencydict)
        queryvector = getQueryVector(query,mode, querydict)
        heap = []

        #calculates dot product between bert query vector and the bert encoded top 1000 relevant document vectors
        for relevantdoc in querydocs:
            documentvector= documentembeddings[relevantdoc][0]
            dotproduct = dotProduct(queryvector,documentvector)
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
    
universalReRank()
