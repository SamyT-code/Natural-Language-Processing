## Introduction
| Name | Assigned Tasks | Student Number |
| ---- | ---- | ---- |
| Samy Touabi | **Preprocessing**, Project Initialization Topic querying, Report | 300184721 |
| Jackie Chen | **Retrieval and Ranking**, Fine-Tuning of Results, Report | 300165909 |
| Kian Zahrai | **Indexing**, Initialized Indexing, Query Processing, Report | 300098986 |
The assignment involves implementing an Information Retrieval (IR) system based on the vector space model for a collection of documents. Key steps include preprocessing (tokenization, stop word removal, stemming), indexing (creating an inverted index), and retrieval and ranking (calculating document-query similarity). In this document, the project is detailed by implementation, methodology, evaluation (using provided queries and relevance judgments), and any observations or conclusions drawn from the process, providing a design to apply theoretical concepts of IR in a practical setting, enhancing understanding of search engine mechanisms.
## Getting Started
---
Following these steps below will guide you to setting up the project and running the programs. The IR system is implemented in Python and is **required** to install the necessary packages used in this project. If not installed on your machine, you can download the installation from the [webpage](https://www.python.org/downloads/). In terms of a specific version, we recommend one of the releases of `3.11` [version](https://www.python.org/downloads/release/python-3118/).

#### Installing Packages
---
The library used to provide support for preprocessing of documents and queries is NLTK. Specifically, the stemming package of NLTK is used to lowers inflection in words to their root forms, hence aiding in the preprocessing of text, words, and documents for text normalization. TO install this package, run the following command (after installation of Python):
```bash
pip install nltk
```

**Note:** Depending upon where the installation is located, the terminal may show an error after running the programs, stating `ModuleNotFoundError: No module named 'nltk'`. As such, run the following command to fix that error:
```bash
py -3 -m pip install nltk
```

#### Program Execution
---
To execute the program, download the assignment zip folder, unzip the folder and open the unzipped file where ever you unzipped it. Open a Terminal (on Linux or Mac) ot Command Prompt (windows) within the unzipped assignment folder. Run the following command (can use `py` or `python` as the launcher option) in Terminal/Command Prompt:
```bash
python main.py
```

To change the mode of testing the queries (titles only or titles + description), change the value of `mode` in `main.py`: `0` --> query on titles, `1` --> query on title + description

Currently `main.py` will load in the `invertedindex.json` file to do help with retrieval. If you would like the index to be remade, delete all files in the helper folder and run the `python main.py` within a Terminal/Command Prompt within the assignment folder. This will take significantly longer.

## Program Functionalities
---
Given the structure of the document collection, test queries and relevance judgments, the following underlines the IR system's need for preprocessing (to handle and index the `<TEXT>` and optionally `<HEAD>` fields), indexing (to manage document identification and facilitate efficient retrieval), and retrieval and ranking (to process queries against the indexed documents and rank them according to relevance). The structure of the project is curated into several Python scripts, text files, and directories that collectively form the Information Retrieval system:

- **Python Files:**
    
    - `main.py`: Serves as the entry point for the project, orchestrating the overall process.
    - `index.py`: Responsible for indexing the documents in the collection.
    - `preprocessor.py`: Intended for preprocessing documents, such as tokenization, stemming, and stop words removal.
    - `queries.py`: Handling the processing of queries, including parsing and preprocessing.
    - `retrieval.py`: Implements the retrieval and ranking logic based on the vector space model.
    
- **Text and HTML Files:**
    
    - `stopwords.txt`: Contains the list of stop words to be excluded during preprocessing.
    - `queries.txt`: Contains the test queries for the IR system.
    - `ideal.txt` and `Results.txt`: Contain relevance judgments and the output results of the IR system, respectively.
    - `Assignment Description.html`: The assignment's description document.
    
- **Directories:**

    - `__pycache__`: Automatically generated cache files, they are compiled versions of the Python scripts and are used to speed up loading times.
    - `coll`: Contains the document collection, comprised of the 322 files.
    - `helper`: The backbone of the IR system, enabling it to quickly process queries and retrieve relevant documents by leveraging the precomputed data structures.
	    - `documentbag.json`: Stores tokenized and possibly preprocessed versions of documents for quick access and retrieval.
	    - `invertedindex.json`: Contains the inverted index mapping terms to documents and their frequencies within those documents, which is crucial for efficient document retrieval.
	    - `maxfrequency.json`: Stores information about the maximum frequency of terms in each document, possibly used for normalization in the retrieval and ranking process.
	    - `vocab.txt`: A list of unique vocabulary terms extracted from the document collection, which is essential for query processing and document indexing.
    - `results`: Stored results of the IR system's performance per running mode in a structured format.

##### `preprocessor.py`
Responsible for preparing the documents and queries for the Information Retrieval (IR) system. Key functionalities include:

- **Word Set Initialization (`getWords`)**: Reads a file (e.g., containing stop words) line by line to initialize a set of words, which is crucial for filtering out stop words during preprocessing.
- **Read File (`readFile`)**: Reads the entire content of a file as a single block of text, facilitating the preprocessing of document and query texts.
- **Remove Punctuation and Lowercasing (`removePunctuation`)**: Cleans the text by removing punctuation, converting words to lowercase, removing digits and standardizing the text for further processing.
- **Tokenization and Stop word Removal (`tokenizeAndRemoveStopWords`)**: Splits the text into tokens (words) and removes stop words, using the list initialized by `getWords`.
- **Stemming (`stemTokens`)**: Applies stemming to the tokens to reduce them to their root form, aiding in the normalization of the text for indexing and retrieval.
	- Leverages the `nltk` library for stemming by combining basic text manipulation techniques with natural language processing tools to prepare text data effectively for IR tasks.


##### `index.py`
Managing the creation of the inverted index (mapping terms to documents), a critical data structure for efficient document retrieval. Key functionalities include:

- **Inverted Index Creation (`makeIndex`)**: Takes a set of vocabulary words and document tokens to create an inverted index. The index maps each word in the vocabulary to the documents it appears in, along with the frequency of the word in each document.
- **JSON Storage (`storeHash`, `retrieveHash`)**: Functions for storing and retrieving the inverted index and other data structures in JSON format, facilitating persistence and reuse of the indexed data.


##### `retrieval.py`
Converting queries and documents into vectors based on the vector space model, to then implement the retrieval and ranking mechanism. Key functionalities include:

- **Query Processing (`runQuery`)**: Processes each query, preparing a query vector and identifying potential documents for retrieval based on the query terms present in the inverted index.
- **Document Ranking (`getRankedDocuments`)**: Ranks the potential documents based on their cosine similarity to the query vector, selecting the top 1000 results for output.


##### `queries.py`
`Query` class to encapsulate the information of each query, including its number (`num`), title (`title`), description (`desc`), and narrative (`narr`). It parses the queries from `queries.txt` and organizes them into a hash table (dictionary) for efficient access. Key functionalities include:

- **Initialization and Parsing**: Initializes query objects and reads them from a file, parsing the relevant sections (`<num>`, `<title>`, `<desc>`, and `<narr>`) to set the attributes of each query object.
- **State Management**: Manages the state (`title`, `desc`, `narr`) to correctly assign parts of the text to the respective attributes of the query object. This is crucial for accurately capturing the multi-part structure of each query.
- **Hash Table Creation**: Optionally creates a hash table (dictionary) mapping query numbers to query objects, facilitating quick access to any query based on its number.


##### `main.py`
Opting for a separation of concerns, as seen in the usage of different Python files for tasks like preprocessing (`preprocessor.py`), indexing (`index.py`), and query processing (`queries.py`), `main.py` ensures modularity and clarity in the project structure, setting up the IR system, from preprocessing documents to indexing and running queries with results output. Key functionalities include:

- **Initialization**: It starts by checking if the helper directory exists and if necessary files are already created. This includes the inverted index, the maximum frequency dictionary, and other preprocessed data stored in the `helper` directory.
- **Mode Selection**: A `mode` variable is used to determine how queries are processed. Mode `0` processes queries based on the title only, while mode `1` uses both the title and description of queries.
- **Query Processing and Retrieval**: If helper files are present, it loads the queries, stop words, inverted index, and maximum frequency dictionary to run the queries. If the helper files are not present, it calls `intializeHelper()` to create these files by processing the corpus, creating the vocabulary, document tokens, index, and other necessary data structures.
- **Making Results File**: The `makesResultsFile` function runs the queries against the indexed documents using the selected mode, stop words, the inverted index, and the maximum frequency dictionary. The results are then formatted and saved to `Results.txt`.
- **Helper Functions**: Includes `intializeHelper` for initializing and creating necessary files and data structures for the IR system, and `printResults` for formatting and outputting the retrieval results.



## Explanation of Algorithms, Data Structures and Optimizations
---
The Information Retrieval (IR) system implemented in the project utilizes a variety of algorithms, data structures, and optimizations to facilitate efficient document processing, indexing, retrieval, and ranking. These elements combined contribute to an IR system that is capable of handling complex queries over large document collections with speed and accuracy. The use of efficient data structures and algorithms, coupled with targeted optimizations, ensures that the system can deliver relevant search results in a timely manner, demonstrating a thoughtful balance between computational efficiency and retrieval effectiveness.


### Preprocessing algorithms
---
- **Tokenization and Normalization**: Splits text into individual terms and normalizes them (e.g., lowercasing). This is fundamental for creating a consistent representation of text data.
- **Stop word Removal**: Excludes common words that offer little value in distinguishing document relevance. This reduces noise in the indexing and retrieval processes.
- **Stemming**: Reduces words to their root form using the Porter Stemming algorithm. This helps in consolidating different forms of a word to a single index entry, enhancing the system's ability to match related terms during queries.


### Indexing algorithms
---
- **Inverted Index Construction**: Utilizes an algorithm to map each term in the vocabulary to a list of documents in which that term appears. This structure is crucial for efficient retrieval, as it allows for rapid lookups of documents relevant to a query term.


### Retrieval and Ranking algorithms
---
- **Vector Space Model (VSM)**: Represents documents and queries as vectors in a multidimensional space, where the relevance is computed using cosine similarity. This algorithm is pivotal for ranking documents based on their relevance to a query.
- **TF-IDF Weighting**: Calculates term frequency-inverse document frequency (TF-IDF) scores to weight the importance of terms within documents and across the corpus. This algorithm enhances the discrimination of term relevance, improving the precision of document ranking.


## Data Structures
---
1. **Sets and Lists**:
    - Used for storing tokens, stop words, and the vocabulary. Sets ensure uniqueness and are used for stop words and vocabulary, while lists may be used for maintaining tokens in their sequential order.
      
2. **Dictionaries (Hash Tables)**:
    - **Inverted Index**: A dictionary maps terms to their document lists, facilitating quick document retrieval for given terms.
    - **Document Frequency and Term Frequency Stores**: These structures keep track of how often terms appear in documents and across the corpus, supporting the computation of TF-IDF scores.
    
3. **JSON Files**:
    - Used to persist inverted indexes, term frequencies, and other metadata on disk. This format allows for structured storage and easy retrieval of preprocessing and indexing results.


## Optimizations
---
- **Preprocessing**:
    - **Efficient Stop word Removal**: By utilizing a set data structure for stop words, the preprocessing algorithm can quickly determine if a token is a stop word in constant time {*O(1)*}. This significantly speeds up the process of filtering out stop words from documents and queries.
    - **Streamlined Text Normalization**: The preprocessing steps likely apply text normalization (such as lowercasing and punctuation removal) in a single pass. This approach minimizes the number of times the text is iterated over, reducing computational overhead.
    
2. **Indexing**:
    - **Batch Processing for Inverted Index Construction**: When constructing the inverted index, the algorithm processes documents in batches. This approach reduces memory usage by avoiding the need to load the entire document collection into memory at once.
    - **Use of Counter Objects for Term Frequency Calculation**: The Python `Counter` class from the `collections` package is used for efficiently counting the occurrence of terms in documents. This allows for rapid calculation of term frequencies (TF) during indexing, which is crucial for the subsequent calculation of TF-IDF scores.
    
3. **Retrieval and Ranking**:
	- **Cosine Similarity Calculation Efficiency**: For calculating cosine similarity between document and query vectors, the algorithm only considers terms that appear in both the query and the document. This reduces the dimensionality of the vectors involved in the calculation, leading to faster similarity computations.
	- **Selective Document Loading**: When retrieving documents based on query terms, the system only loads document information that is necessary for ranking (e.g., term frequencies, document lengths) rather than the full document text. This significantly decreases the amount of data processed during retrieval.
	- **Early Termination in Ranking**: In the ranking process, an early termination strategy is employed, where documents are sorted by their potential relevance (e.g., based on the number of query terms they contain) and the system stops considering documents beyond a certain threshold. This reduces the number of documents that need to be fully evaluated for relevance.
	  
4. **General**:
	- **Caching**: Caching mechanisms  implied in various stages of the IR system (e.g., caching the results of frequent queries or intermediate preprocessing steps) to reduce computation times for repetitive operations.
	- **Data Structure Choices**: The choice of data structures (e.g., dictionaries for the inverted index, sets for stop words) is inherently an optimization, as these structures are chosen for their efficiency in specific operations required by the IR system.


## Vocabulary
---
The `vocab.txt` file contains the vocabulary of the corpus, a list of unique terms extracted from the document collection during the preprocessing phase. The size of the vocabulary (being of `123058` terms and `1.071 MB` in size) impacts system performance, with a larger vocabulary potentially offering more precise retrieval at the cost of increased computational requirements.

1. **Indexing Efficiency**: By maintaining a list of unique terms, the IR system can efficiently create and update its inverted index. This index is crucial for mapping terms to the documents in which they appear, facilitating quick retrieval of relevant documents based on query terms.
    
2. **Query Processing**: Having a predefined vocabulary helps in processing queries by quickly determining which terms in a query are present in the document collection. This aids in filtering out terms that do not contribute to document retrieval and focusing on those that do.
    
3. **Dimensionality Reduction**: In vector space models and other algorithms that represent documents and queries as vectors, the vocabulary size determines the dimensionality of these vectors. By managing the vocabulary, the system can mitigate issues related to high dimensionality, such as computational complexity and the curse of dimensionality.
    
4. **Term Frequency and Weighting Calculations**: The vocabulary supports the calculation of term frequency (TF) and inverse document frequency (IDF) values, which are essential for ranking documents in relevance to a query. Knowing the full set of terms allows for accurate TF-IDF weighting across the document collection.
    
5. **Consistency and Optimization**: The `vocab.txt` file ensures consistency in term usage across the IR system. It also enables optimizations like precomputing and caching term-related statistics for faster retrieval and ranking operations.

##### Sample of 100 Tokens
```plaintext
phd, cullen, rohmer, bankrupci, plutarco, tripoli, wymon, farceur, peven, acknowledg, mansouri, pitiabl, glycol, yadin, sacco, mahn, rone, zhelaniya, kirthibahu, gainov, pattamasrikaew, nakamaru, viraj, devillar, bachmeier, kaifeng, fytraki, pavon, consequt, unchurch, undeciph, feraud, soprano, geiger, unchart, tongass, wamala, remun, pastor, compris, overbroad, alhough, hypothyroid, vehcil, copehnagen, altair, heyding, agno, squalid, remp, sachar, kyaw, sundan, terreri, paag, posess, unapprais, lattest, yazejeh, soem, kath, sukhudreyev, ugolin, honkytonk, raboso, rummi, deffici, schmutzler, zofia, lamaken, mangeus, shibani, harrier, precautionari, mattei, upazila, unstartl, ashot, unaccept, spontan, rabbl, gaieti, interoffic, magariaf, mcbee, huachuca, sabbat, biodegrad, globeberri, bildner, yeremoni, takagi, financi, clabir, feynman, bitterlin, gaberdeen, lutgen, sbo, udayapur, snowcrest
```


## Discussion of Results
---
The provided outputs from `trec_eval` give us an insight into how the Information Retrieval (IR) system implemented performs against the set of queries and the ideal query relevancies. The `trec_eval` tool is widely used for evaluating the effectiveness of IR systems, providing metrics such as Mean Average Precision (MAP), precision at various recall levels, and overall precision for different cutoffs. The commands used to run the `trec_eval` script for the IR system is the following (**`trec_eval` must be installed on the machine beforehand**):
This outputs overall assessment:
```bash
trec_eval ideal.txt Results.txt
```

And this outputs the MAP scores for each query:
```bash
trec_eval -q -m map ideal.txt Results.txt
```

The `trec_eval` scores provided from evaluating the IR system using `ideal.txt` (relevance judgments) and `Results.txt` (system rankings) reveal two key observations:

1. **MAP Score for Title Only (`mode=0`)**: The Mean Average Precision (MAP) score when querying with only the title is `0.1677`. This score represents the average precision across all queries, providing a measure of the system's effectiveness in retrieving relevant documents based on query titles alone, revealing a key indicator of the overall effectiveness of the retrieval process across all queries.
2. **MAP Score for Title and Description (`mode=1`)**: When the system queries using both titles and descriptions, the MAP score improves to `0.2273`. This indicates a higher performance in document retrieval and relevance ranking, showing that including descriptions in queries helps in retrieving more relevant documents.
3.  **R-precision (`Rprec`)**: `0.1820` and `0.2353` for modes `0` and `1` respectively, indicating the precision after R documents have been retrieved, where R is the number of relevant documents for a query.
4. **Precision at different levels of retrieved documents (P_5, P_10, etc.)**, which shows how precision changes as more documents are considered. 

| Precision Level (mode 0) | Score | Precision Level (mode 1) | Score |
| ---- | ---- | ---- | ---- |
| P_5 | 0.2120 | P_5 | 0.3560 |
| P_10 | 0.1820 | P_10 | 0.2840 |
| P_15 | 0.1693 | P_15 | 0.2667 |
| P_20 | 0.1580 | P_20 | 0.2560 |
| P_30 | 0.1527 | P_30 | 0.2320 |
| P_100 | 0.1066 | P_100 | 0.1478 |
| P_200 | 0.0822 | P_200 | 0.0969 |
| P_500 | 0.0424 | P_500 | 0.0503 |
| P_1000 | 0.0270 | P_1000 | 0.0292 |

These scores suggest that the IR system performs better when more context (i.e., title and description) is provided in the queries. This indicates that including more contextual information from the "description" tag alongside the "title" enhances the system's ability to retrieve relevant documents, leading to a better overall performance. This aligns with the intuitive understanding that additional query information can aid in the retrieval of more relevant documents. To exemplify the findings, queries 1 and 25 are delved in deeper to understand the MAP scores associated with them;
###### Query 1:

- **Title**: Coping with overcrowded prisons
- **Description**: Seeks information on jail and prison overcrowding, how inmates cope, or plans to alleviate the condition.
- **Narrative**: Relevant documents will describe scenes of overcrowding in jails and prisons, how inmates are forced to cope with these conditions, and what the Correctional System is doing or planning to do to alleviate the crowded condition.
- **MAP Score - Title only (`mode=0`)**: 0.2454
- Top 10 Ranking
```plaintext
1 Q0 AP880310-0051 1 0.9487104820841753 r1
1 Q0 AP880519-0231 2 0.9487104820841753 r1
1 Q0 AP881216-0222 3 0.9487104820841752 r1
1 Q0 AP880906-0154 4 0.9487104820841751 r1
1 Q0 AP880526-0013 5 0.948710482084175 r1
1 Q0 AP880218-0255 6 0.7864773586854242 r1
1 Q0 AP880405-0072 7 0.7864773586854242 r1
1 Q0 AP880608-0251 8 0.7864773586854242 r1
1 Q0 AP880216-0195 9 0.7864773586854241 r1
1 Q0 AP880219-0042 10 0.7864773586854241 r1
```

- **MAP Score - Title and Description (`mode=1`)**: 0.3769
- Top 10 Ranking
```plaintext
1 Q0 AP881108-0076 1 0.8137141954956544 r2
1 Q0 AP881122-0004 2 0.8012563678346795 r2
1 Q0 AP881216-0222 3 0.7860163176631367 r2
1 Q0 AP881122-0059 4 0.7835241058470532 r2
1 Q0 AP881223-0053 5 0.7786497446870811 r2
1 Q0 AP880218-0137 6 0.7756902380115832 r2
1 Q0 AP880219-0031 7 0.7756902380115832 r2
1 Q0 AP880218-0105 8 0.7697418063098211 r2
1 Q0 AP880704-0017 9 0.7691510959561877 r2
1 Q0 AP880827-0151 10 0.7591059661490218 r2
```

###### Query 25:

- **Title**: NRA Prevention of Gun Control Legislation
- **Description**: The document reports on instances where the NRA engaged in actions to prevent the passage of legislation aimed at reducing gun proliferation.
- **Narrative**: Relevant documents include specific instances where gun control legislation was defeated through the NRA's efforts, including influencing popular votes and legislator lobbying.
- **MAP Score - Title only (`mode=0`)**: 0.1293
- Top 10 Ranking
```plaintext
25 Q0 AP880511-0289 1 0.9981674102460556 r1
25 Q0 AP880811-0163 2 0.9838053111889957 r1
25 Q0 AP880622-0068 3 0.9836195196539713 r1
25 Q0 AP880429-0040 4 0.980527919832043 r1
25 Q0 AP880803-0033 5 0.9711857058972589 r1
25 Q0 AP880630-0204 6 0.9484693001255516 r1
25 Q0 AP880810-0116 7 0.9479937369889878 r1
25 Q0 AP881123-0114 8 0.9476030046244962 r1
25 Q0 AP880518-0048 9 0.9473433577529524 r1
25 Q0 AP880929-0184 10 0.9468080225495635 r1
```

- **MAP Score - Title and Description (`mode=1`)**: 0.1850
- Top 10 Ranking
```plaintext
25 Q0 AP880429-0040 1 0.789326255017765 r2
25 Q0 AP880310-0257 2 0.7827888045341268 r2
25 Q0 AP880811-0163 3 0.7641057920909661 r2
25 Q0 AP880605-0026 4 0.7583653225506111 r2
25 Q0 AP880606-0019 5 0.7575444832692653 r2
25 Q0 AP880803-0033 6 0.7549880642336123 r2
25 Q0 AP880424-0020 7 0.7519618074500976 r2
25 Q0 AP880413-0242 8 0.7505766619634642 r2
25 Q0 AP880511-0289 9 0.7415421037418407 r2
25 Q0 AP880622-0068 10 0.7308674199142938 r2
```

Given these results for queries 1 and 25, when running with "title" only, the cosine similarity scores for query 25 performed higher and more consistently than query 1, meaning that there are more words in common in between query 25 and the collection of documents than between query 1 and the collection. However, when running with "title" and "description", both queries perform about the same manner (even though query 1 starts off superior). Since query title and description give a larger vocabulary of words, it allows for more similarities between query 1 and 25 and the collection than before.

Using `trec_eval`, even the number of relevant documents using title only is less than when using title and description (`1350` from `2099` vs `1458`). All in all, the MAP score is superior when title and description provides a larger vocabulary, which leads to more similarities detected between the collection of documents and the query. For further comparison and viewing of results, a `results` directory is provided.


## Extra
- **Document Collection**: `AP_readme` is an outline stating that the collection of documents `coll` consists of 79,923 documents from the Associated Press (1988), grouped in 322 files. The main content to be indexed is within the `<TEXT>` field of each document, with the option to also use the `<HEAD>` field. Documents are uniquely identified by a code in the `<DOCNO>` field. Each document is comprised of the following information:
	- **Start of Document**: Each document begins with a `<DOC>` tag.
	- **Document Number**: Identified by the `<DOCNO>` tag, which uniquely identifies each document (e.g., `AP880212-0001`).
	- **File ID**: Marked by the `<FILEID>` tag, providing additional identification details.
	- **First Line**: Identified with a `<1ST_LINE>` tag, potentially offering summary or key information.
	- **Second Line**: Similar to the first line, marked with a `<2ND_LINE>` tag.
	- **Headline**: The `<HEAD>` tag encapsulates the document's headline or title.
	- **Dateline**: The `<DATELINE>` tag provides the location and date information.
- **Text Content**: Enclosed within the `<TEXT>` tags, this section contains the main body of the document.
- **Test Queries**: `queries.txt` is a set of 50 test topics, each with a number, a title, a description, and a narrative. For query processing, you can use the content from the `<title>`, `<desc>`, and `<narr>` fields to extract keywords, depending on the level of detail preference.
- **Relevance Judgments**: Provided in the `ideal.txt` file, these include binary relevance scores for evaluating the IR system's performance on the test topics. The format used is suitable for the `trec_eval` tool, with each line containing a topic number, a dummy column (always zero), a document code (`DOCNO`), and a binary relevance score (0 or 1), sorted by topic.


## Future Works for Improvement
To achieve higher performance scores in the Information Retrieval (IR) system, the following areas can be considered for improvement:

1. **Weighting Scheme**: While an improved TF-IDF scheme provides a solid foundation, exploring alternative weighting schemes like **BM25**, which accounts for document length and term frequency saturation, could offer better relevance scoring.
    
2. **Lemmatization**: Incorporating lemmatization could improve the query and document processing by reducing words to their base or dictionary form, potentially increasing match accuracy over simple stemming.
    
3. **Semantic Analysis**: Integrating semantic analysis tools or techniques, such as Latent Semantic Analysis (LSA) or word embeddings (**Word2Vec**, **GloVe**), could enhance the system's ability to understand the meaning behind queries and documents.
    
4. **Advanced IR Frameworks**: Utilizing established IR frameworks like **PyTerrier**, which provides a Python interface to the powerful Terrier IR platform, could leverage advanced indexing, retrieval, and ranking features, along with a wide array of existing research and optimizations.
