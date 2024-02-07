
# Import modules
from queries import Query
from retrieval import runQuery
from vocabvector import Vocabvector
from index import retrieveHash
from preprocessor import getWords
import os

# Initialize objects 
queries_data = Query.read_queries('testing_files/queries.txt')
stopwords = getWords("testing_files/stopwords.txt")
index = retrieveHash("testing_files/invertedindex.json")
documentbag = retrieveHash("testing_files/documentbag.json")

def main():
    mode = 0 #0 = query on the title, 1 = query title + description
    count = 0
    results = []
    for query in queries_data:
        results.append(runQuery(queries_data[query].num, mode, queries_data, stopwords, index,documentbag))
        count += 1
        print(str(count) + "/ 50 queries done")
    
    if os.path.exists("Results.txt"):
        os.remove("Results.txt")
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
                file.write(str(x+1)+ " Q0 "+ results[x][y][1]+" "+ str(count)+ " "+ str(results[x][y][0])+" "+ runname + "\n")
            count = 0
#main 
print("Done initializing")
main()
