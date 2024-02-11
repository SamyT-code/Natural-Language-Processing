
# Import modules
from queries import Query
from retrieval import runQuery, getCosineSimilarity
from index import retrieveHash,storeHash,makeIndex
from preprocessor import getWords,processCorpus
import os


def checkHelperDirectory(directoryname):
    try:
        if any(os.scandir(directoryname)):
            return True
    except (NotADirectoryError, FileNotFoundError):
        pass
    return False

def main():
    print("Start")

    #change mode to 0 to query on the queries title
    #change mode to 1 to query on the queries title and description
    mode = 0

    if checkHelperDirectory('helper/'):
        print("Helper files already made")

        # intialize needed objects from helper directory
        queries_data = Query.read_queries('queries.txt')
        stopwords = getWords("stopwords.txt")
        index = retrieveHash("helper/invertedindex.json")
        maxfrequencydict = retrieveHash("helper/maxfrequency.json")

        #run the queries 
        makesResultsFile(queries_data,mode,stopwords,index,maxfrequencydict)
    else: 
        intializeHelper()

         # intialize needed objects from helper directory
        queries_data = Query.read_queries('queries.txt')
        stopwords = getWords("stopwords.txt")
        index = retrieveHash("helper/invertedindex.json")
        maxfrequencydict = retrieveHash("helper/maxfrequency.json")

        #run the queries 
        makesResultsFile(queries_data,mode,stopwords,index,maxfrequencydict)
        print("Results in Results.txt")

def intializeHelper():
    stopwords = getWords("stopwords.txt")

    documentdictonary = {}
    index = {}
    maxfrequency = {}
    vocabset = set()
    
    processCorpus(documentdictonary,vocabset,stopwords)
    print("vocabulary and document tokens made")
    index, maxfrequency = makeIndex(vocabset,documentdictonary)
    print("Index and Maxfrequency created")

    with open("helper/vocab.txt","w") as file:
        for word in vocabset:
            file.write(word+"\n")
    print("helper/vocab.txt created")
    
    storeHash(documentdictonary, "helper/documentbag.json")
    print("helper/documentbag.json created")

    storeHash(index, "helper/invertedindex.json")
    print("helper/invertedindex.json created")

    storeHash(maxfrequency,"helper/maxfrequency.json")
    print("helper/maxfrequency.json created")

    print("All helper files created")
    
def makesResultsFile(queries_data,mode,stopwords,index,maxfrequencydict):
    results = []
    for query in queries_data:
        results.append(runQuery(queries_data[query].num, mode, queries_data, stopwords, index,maxfrequencydict))

    print("Finshed running queries")    
    if os.path.exists("Results2.txt"):
        os.remove("Results2.txt")
        printResults(results, mode)
    else:
        printResults(results, mode)
    
def printResults(results,querytype):
    runname= ""
    match querytype:
        case 0:
            runname = "r1" # query only title
        case 1:
            runname = "r2" #query title and description

    with open("Results.txt","w") as file:
        count = 0
        for x in range(len(results)):
            for y in range(len(results[x])):
                count += 1
                file.write(str(x+1)+ " Q0 "+ str(results[x][y][1])+" "+ str(count)+ " "+ str(results[x][y][0])+" "+ runname + "\n")
            count = 0

#main
main()
