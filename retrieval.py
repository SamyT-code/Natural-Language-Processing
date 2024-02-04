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
        ->if token in list a is in inverted index, add the keys on the inner document dictiornary to set A
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
compute similairty between docvecotr and query vector and sort the result

->make a max heap using python heapq ( built in library) 
-> interate through doc vectors
    -> run vocabvector.cosinesimilairty(queryvector,doc vectors)
    -> add {docname: reulst of cosinesimilairty } into the heap
-> once all docs similarity computed, pop the first 1000 results into a text file 
        









'''