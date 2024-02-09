
# Import modules
from queries import Query
from retrieval import runQuery, getCosineSimilarity
from index import retrieveHash
from preprocessor import getWords
import os


# Initialize objects 
queries_data = Query.read_queries('testing_files/queries.txt')
stopwords = getWords("testing_files/stopwords.txt")
index = retrieveHash("testing_files/invertedindex3.json")
documentbag = retrieveHash("testing_files/documentbag3.json")
maxfrequencydict = retrieveHash("testing_files/maxfrequency.json")

def main():
    mode = 0 #0 = query on the title, 1 = query title + description
    count = 0
    results = []

    for query in queries_data:
        results.append(runQuery(queries_data[query].num, mode, queries_data, stopwords, index,maxfrequencydict))
        count += 1
        print(str(count) + "/ 50 queries done")
    
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

    with open("Results2.txt","w") as file:
        count = 0
        for x in range(len(results)):
            for y in range(len(results[x])):
                count += 1
                file.write(str(x+1)+ " Q0 "+ str(results[x][y][1])+" "+ str(count)+ " "+ str(results[x][y][0])+" "+ runname + "\n")
            count = 0
#main 
main()
'''
query1, tokens, queryvector, documents = runQuery(1, 0, queries_data, stopwords, index,maxfrequencydict )
print(tokens)
print(queryvector)
print(queryvector.get("overcrowd"))
#print(documents.get('AP880526-0013'))
print(documents.get('AP881202-0169'))
print(getCosineSimilarity(queryvector,documents.get('AP881202-0169'),tokens))
print()
'''