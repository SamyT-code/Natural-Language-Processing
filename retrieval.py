'''
step 1
turn query into a vocab vector 
    ->run query.py to get queries user specifes 
    -> concatenate title/description/narrative text into 1 big text (called Bigtext)
    -> use Tokenizedoc(Bigtext (found in preprocessor.py) to list of tokens (call it List B) 
        ->make a list containing only 1 copy of each token (call it list A), run VocabVector.setWords(List A)
        ->create queryvector = vocabvector() and run a for loop through listb doing queryvector.setVectorValue(Listb[i]) 
        //might have to tweak setVectorValue, havent tested it yet


step 2
get all the documents that contain at least 1 word from list A
    -> load in index using retrieveHash() from index.py
    ->create a set that will store the doucments that will be look through (call it set A)
    -> iterate through the list a
        ->if token in list a is in testing_files/invertedindex.json, add the keys on the inner document dictiornary to set A
        else, ignore the token

        
step 3
turn the docs from list A to queryvectors
    -> create a hash map with key = doc name, value = vocabvector (call it Doc vectors)
    -> load in the documentbag using retrieveHash() from index.py
    -> iterate through setA
        -> create docvector = vocabvector() and run a for loop through docmuents tokens ( call it bag)
            ->if the tokens in doc match the tokens in vocabcvecotr.words, docvector.setVectorValue(token,calculateTfidfWeight(cls,tf, n, df))
        //might have to tweak setVectorValue, havent tested it yet

step 4
compute similairty between docvector and query vector and sort the result

->make a max heap using python heapq ( built in library) 
-> interate through doc vectors
    -> run vocabvector.cosinesimilairty(queryvector,doc vectors)
    -> add {docname: reulst of cosinesimilairty } into the heap
-> once all docs similarity computed, pop the first 1000 results into a text file 
'''

# Import modules
from queries import Query
from preprocessor import tokenizeDoc, getWords
from vocabvector import Vocabvector
from index import retrieveHash

# Initialize objects 
queries_data = Query.read_queries('queries.txt')
stopwords = getWords("testing_files/stopwords.txt")
index = retrieveHash("testing_files/invertedindex.json")
documentbag = retrieveHash("testing_files/documentbag.json")




'''
# Initialize Bigtext as an empty string
Bigtext = ""

# Concatenate the title, description, and narrative text into Bigtext
for query in queries_data:
    Bigtext += f"Title: {query.title}\n"
    Bigtext += f"Description: {query.desc}\n"
    Bigtext += f"Narrative: {query.narr}\n"
    Bigtext += "\n"  # Add a blank line between queries

# Print or use Bigtext as needed
# print(Bigtext)
'''

def runQuery(querynumber):
    # Split Bigtext into individual queries using blank lines as separators
    query_texts = Bigtext.split('\n\n')

    # Check if the specified query number is within the valid range
    if querynumber < 1 or querynumber > len(query_texts):
        print(f"Query number {querynumber} is out of range.")
        return

    # Get the query text for the specified query number
    query_text = query_texts[querynumber - 1]

    # Print the query text
    print(query_text)

# # Example usage:
# query_number = 10  # Replace with the desired query number

'''
# Tokenize the Bigtext using Tokenizedoc
document_tokens = tokenizeDoc(Bigtext, stopwords)
'''

#querytype: 0 = title , 1 = title + doc
def  prepareQueryVector(querynumber, querytype,querylist):
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

        return queryvector

def getPotentialDocuments(querytokens,index):
    potentialdocuments = set()
    for token in querytokens:
        if index.get(token) != None:
            potentialdocuments.update(set(index.get(token).keys()))
    return potentialdocuments

def getDocumentvector(querytokens,index,document):
    documentqueryvector= Vocabvector()
    for token in querytokens:
        if index.get(token) != None:
            if document in index.get(token):

        
    
#main 
queryvector = prepareQueryVector(50,0,queries_data)
potentialdocuments = getPotentialDocuments(Vocabvector.words,index)

'''
# Create List B (contains all tokens)
ListB = document_tokens

# Create List A (contains unique tokens)
ListA = list(set(ListB))

# Create a VocabVector object and set its words

# from vocabvector import calculateTfidfWeight
vocab_vector = Vocabvector()
vocab_vector.setWords(ListA)

# Create a queryvector object and set its vector values
queryvector = Vocabvector()
for token in ListB:
     queryvector.setVectorValue(token, queryvector.vector[vocab_vector.words.index(token)] + 1) 

# Now, queryvector contains the vector values for List B tokens

# Step 2: Get documents containing at least 1 word from List A

# Create a set to store documents to be looked through (set A)
setA = set()

# Iterate through List A tokens
for token in ListA:
    if token in index:
        # Add the keys from the inner document dictionary to set A
        setA.update(index[token].keys())

# Now, setA contains the documents that contain at least 1 word from List A

# Step 3: Turn the docs from List A into queryvectors
# Create a hash map with key = doc name, value = vocabvector (call it Doc vectors)
DocVectors = {}

# Calculate document frequency (df) for each token in ListA
token_df = {}
for token in ListA:
    token_df[token] = sum(1 for doc in documentbag.values() if token in doc)

# Iterate through setA
for doc_name in setA:
    doc_tokens = documentbag.get(doc_name, [])
    doc_vector = Vocabvector()
    
    # Run a for loop through document tokens (bag)
    for token in doc_tokens:
        if token in vocab_vector.words:
            # Set vector value with TF-IDF weight using precomputed df
            tf = doc_tokens.count(token)
            tfidf_weight = vocab_vector.calculateTfidfWeight(tf, len(documentbag), token_df[token])
            doc_vector.setVectorValue(token, tfidf_weight)
    
    # Add the doc vector to DocVectors
    DocVectors[doc_name] = doc_vector


# Now, DocVectors contains queryvectors for documents in List A


# Step 4
import heapq

# Create a max heap to store the top 1000 results
result_heap = []

# Iterate through doc vectors
for doc_name, doc_vector in DocVectors.items():
    # Compute cosine similarity between query vector and doc vector
    similarity = vocab_vector.cosineSimilarity(queryvector, doc_vector)
    
    # Add (similarity, doc_name) tuple to the heap
    heapq.heappush(result_heap, (similarity, doc_name))

# Pop the first 1000 results from the heap
top_1000_results = heapq.nlargest(1000, result_heap)

# Create a text file to store the results
with open('top_1000_results.txt', 'w') as file:
    for similarity, doc_name in top_1000_results:
        file.write(f'Document: {doc_name}, Similarity: {similarity}\n')

# Now, the top 1000 results sorted by similarity are stored in 'top_1000_results.txt'
'''