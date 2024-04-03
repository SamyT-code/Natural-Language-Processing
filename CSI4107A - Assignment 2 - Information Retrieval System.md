## Introduction


| Name        | Assigned Tasks                                                            | Student Number |
| ----------- | ------------------------------------------------------------------------- | -------------- |
| Samy Touabi | Implementation of **BERT** & **Universal Sentence Encoder** Neural Models | 300184721      |
| Jackie Chen | Implementation of **BERT** & **Universal Sentence Encoder** Neural Models | 300165909      |
| Kian Zahrai | **Report Documentation** & Fine-Tuning of Results                         | 300098986      |

The second part of the assignment involves incorporating advanced neural language models into the IR system, focusing on the same document collection. This approach aims to enhance the system's understanding and processing of natural language, potentially improving query relevance and document ranking performance. In this document, the project is detailed by implementation, methodology, evaluation (using provided queries and relevance judgments), and any observations or conclusions drawn from the process, providing a design to apply theoretical concepts of IR in a practical setting, enhancing understanding of search engine mechanisms.

Aside from the previous key steps (preprocessing {tokenization, stop word removal, stemming}, indexing {creating an inverted index}, and retrieval and ranking {calculating document-query similarity}, the project explores techniques such as embeddings, which represent words and documents in dense vector spaces, and transformer-based models like **BERT** or **GPT**, which are capable of capturing deep semantic relationships within text. The inclusion of these models can significantly improve the IR system's ability to understand query intent and document context, leading to more accurate and relevant search results.

## Getting Started
---
Following these steps below will guide you to setting up the project and running the programs. The IR system is implemented in Python and is **required** to install the necessary packages used in this project. If not installed on your machine, you can download the installation from the [webpage](https://www.python.org/downloads/). In terms of a specific version, we recommend one of the releases of `3.11` [version](https://www.python.org/downloads/release/python-3118/).

#### Installing Packages
---
The library used to provide support for term embeddings is `SentenceTransformer`. However, the `nltk` library is still necessary for the preprocessing of documents and queries. The framework used to compute dense vector representations for sentences and paragraphs based on transformer networks like **BERT**. The text is embedded in vector space such that similar text are closer and can efficiently be found using cosine similarity. To install this package, run the following command (after installation of Python):

```bash

pip install sentence-transformers

```


**Note:** Depending upon where the installation is located, the terminal may show an error after running the programs, stating `ModuleNotFoundError: No module named 'sentence-transformers'`. As such, run the following command to fix that error:

```bash

py -3 -m pip install sentence-transformers

```

  
#### Program Execution
---
To execute the program, download the assignment zip folder, unzip the folder and open the unzipped file where ever you unzipped it. Open a Terminal (on Linux or Mac) or Command Prompt (Windows) within the unzipped assignment folder. Run the following commands (can use `py` or `python` as the launcher option) in Terminal/Command Prompt;

To run the Python program regarding the **BERT** model:
```bash
python distilbert.py
```

To run the Python program regarding the **Universal Sentence Encoder** model:
```bash
python universal.py
```

To change the mode of testing the queries (titles only or titles + description), change the value of `mode` in each of the above Python programs: `0` --> query on titles, `1` --> query on title + description

  
Currently `cosine.py` will load in the `invertedindex.json` file to do help with retrieval. If you would like the index to be remade, delete all files in the `helper` folder and run the following within a Terminal/Command Prompt within the assignment folder. This will take significantly longer.
```bash
python cosine.py
```

  
## Program Functionalities
---
Given the structure of the document collection, test queries and relevance judgments, the following underlines the IR system's need for preprocessing (to handle and index the `<TEXT>` and optionally `<HEAD>` fields), indexing (to manage document identification and facilitate efficient retrieval), and retrieval and ranking (to process queries against the indexed documents and rank them according to relevance), as well as adopting neural models. The methodology implied here involves using advanced NLP models to convert text data into embeddings that represent the semantic content of the queries and documents. This approach allows the IR system to perform retrieval based on the meaning of the text rather than just matching keywords, potentially improving the relevance of the retrieved documents to the queries. The structure of the project is curated into several Python scripts, text files, and directories that collectively form the Information Retrieval system:


- **Python Files:**

    - `cosine.py`: Serves as the entry point for the project, orchestrating the overall process. Renamed from `main.py`, this module is for computing cosine similarity between documents and queries, crucial for the retrieval and ranking phase.
    - `distilbert.py` and `universal.py`: Implement neural model approaches for IR, utilizing ***DistilBERT*** and ***Universal Sentence Encoder*** for semantic similarity.
    - `index.py`: Responsible for indexing the documents in the collection, creating the inverted index.
    - `preprocessor.py`: Intended for preprocessing documents, such as tokenization, stemming, and stop words removal.
    - `queries.py`: Handling the processing of queries, including parsing and preprocessing, as well as reformulating queries for improved retrieval.
    - `retrieval.py`: Implements the retrieval and ranking logic based on the vector space model (utilizing the inverted index to find relevant documents based on queries and ranking them).

- **Text and HTML Files:**

    - `stopwords.txt`: Contains the list of stop words to be excluded during preprocessing (to eliminate common, non-informative words from text data).
    - `queries.txt`: Contains the test queries for the IR system as query inputs.
    - `ideal.txt` and `Results.txt`: Contain relevance judgments and the output results of the IR system, respectively.
    - `Assignment1 Description.html`: The first part of the assignment's description document.
    - `Assignment2 Description.html`: The second part of the assignment's description document.

- **Directories:**

    - `__pycache__`: Automatically generated cache files, they are compiled versions of the Python scripts and are used to speed up loading times.
    - `coll`: Contains the raw document collection, comprised of the 322 files. Organized by date, each file in this directory represents a set of news articles from a specific day.
    - `helper`: The backbone of the IR system, enabling it to quickly process queries and retrieve relevant documents by leveraging the precomputed data structures.

        - `documentbag.json`: Stores tokenized and possibly preprocessed versions of documents for quick access and retrieval, by representing documents as a bag of words.
        - `documenttext.json`: Contains a more human-readable summary or tag for each document, providing a comprehensive summary of the document's content, maintaining the order and readability of the original text.
        - `DocEncode.ipynb` and `QueryEncode.ipynb`: Used for preprocessing the queries and documents, respectively, by encoding their textual content into numerical representations, to help with computing semantic similarities between queries and documents beyond simple keyword matching.
        - `queries.json`: Raw text of the queries, including titles, descriptions, and narratives for each query ID, serving as the input for `QueryEncode.ipynb`, where each query is then encoded into a numerical format suitable for neural models.
        - `universalqueries.json` and `embedbertqueries.json`: Contain the encoded representations of the queries, generated by different models as suggested by their names. The encoding process transforms the textual information into vectors that capture the semantic meaning of each query, enabling more sophisticated retrieval mechanisms that can account for the context and nuances of the queries.
        - `universaldocuments.json`: Storing numerical representation of documents using embeddings, associated with a high-dimensional vector that captures the semantic essence of the document's content.
        - `invertedindex.json`: Contains the inverted index mapping terms to documents and their frequencies within those documents, which is crucial for efficient document retrieval (A precomputed inverted index, stored in JSON format for quick loading during the retrieval process).
        - `maxfrequency.json`: Stores information about the maximum frequency of terms in each document, used for normalization of term frequencies or weights during the indexing, retrieval and ranking processes, enhancing the effectiveness of both traditional and neural retrieval approaches.
        - `vocab.txt`: A list of unique vocabulary terms extracted from the document collection, which is essential for query processing and document indexing.

    - `results`: Stored results of the IR system's performance per running mode in a structured format.


##### `preprocessor.py`

Responsible for preparing the documents and queries for the Information Retrieval (IR) system. Key functionalities include:

- **Word Set Initialization (`getWords`)**: Reads a file (e.g., containing stop words) line by line to initialize a set of words, which is crucial for filtering out stop words during preprocessing.
- **Read File (`readFile`)**: Reads the entire content of a file as a single block of text, facilitating the preprocessing of document and query texts.
- **Removal of Unwanted Elements (`removeUnwanted`)**: It strips digits, converts text to lowercase, replaces punctuation with spaces, and splits the text into tokens. It also removes stop words and non-alphabetic tokens, streamlining the dataset to meaningful words only.
- **Tokenization and Stemming (`stemTokens`)**: After cleaning the text, it splits the content into individual words (tokens) and applies stemming to reduce words to their base or root form using the Porter Stemmer algorithm. This helps in treating different forms of a word as equivalent during search queries.
- **Document Processing (`processFile`**: Each document's unique identifier (`<DOCNO>`) and textual content (`<TEXT>` and `<HEAD>`) are extracted. The text is then preprocessed and stemmed, and the tokens are organized for indexing.
- **Corpus Processing (`processCorpus`)**: It iterates through each file in the collection, processes each document, and compiles a vocabulary set and a dictionary of documents with their tokens. This step is foundational for creating an efficient index.
  
##### `index.py`

Managing the creation of the inverted index (mapping terms to documents), a critical data structure for efficient document retrieval. Key functionalities include:

- **Inverted Index Creation (`makeIndex`)**: Takes a set of vocabulary words and document tokens to create an inverted index. For each token in the vocabulary, it constructs an entry in the index that maps the token to documents containing it, along with the frequency of the token in each document.
- **Maximum Frequency Calculation**: Tracks the highest frequency count of any term in each document, which is critical for normalizing term frequency during the retrieval process.
- **JSON Storage (`storeHash`, `retrieveHash`)**: Utility functions for storing and retrieving the inverted index and other data structures in JSON format, facilitating persistence and reuse of the indexed data.

##### `retrieval.py`

Converting queries and documents into vectors based on the vector space model, to then implement the retrieval and ranking mechanism (querying the index to find relevant documents and rank them based on their similarity to the query). Key functionalities include:

- **Query Processing and Preparation (`runQuery` and `runReRankQuery`)**: Processes each query, preparing a query vector and identifying potential documents for retrieval based on the query terms present in the inverted index, where each token is weighted by its TF-IDF score.
- **Document Ranking and Reranking (`getRankedDocuments` & `getReRankedDocuments`)**: Ranks the potential documents based on their cosine similarity to the query vector, selecting the top 1000 results for output. The Re-ranking returns a list of documents ordered by their relevance to the query, based on the computed cosine similarity scores.
- **Cosine Similarity Calculation (`getCosineSimilarity`)**: Employs the dot product and magnitude of vectors to calculate cosine similarity, a measure that quantifies how closely related a document is to the query.


##### `queries.py`

`Query` class to encapsulate the information of each query, including its number (`num`), title (`title`), description (`desc`), and narrative (`narr`). It parses the queries from `queries.txt` and organizes them into a hash table (dictionary) for efficient access. Key functionalities include:  

- **Initialization and Parsing**: Initializes query objects and reads them from a file, parsing the relevant sections (`<num>` for query number, `<title>` for query title, `<desc>` for query description, and `<narr>` for query narrative) to set the attributes of each query object.
- **State Management**: Manages the state (`title`, `desc`, `narr`) to correctly assign parts of the text to the respective attributes of the query object. This is crucial for accurately capturing the multi-part structure of each query.
- **Hash Table Creation**: Creates a hash table (dictionary) mapping query numbers to query objects, facilitating quick access to any query based on its number.


##### `cosine.py`

Opting for a separation of concerns, as seen in the usage of different Python files for tasks like preprocessing (`preprocessor.py`), indexing (`index.py`), and query processing (`queries.py`), `cosine.py` ensures modularity and clarity in the project structure, setting up the IR system, from preprocessing documents to indexing and running queries with results output. Key functionalities include:

- **Initialization**: It starts by checking if the helper directory exists and if necessary files are already created. This includes the inverted index, the maximum frequency dictionary, document bags and other preprocessed data stored in the `helper` directory.
- **Mode Selection**: A `mode` variable is used to determine how queries are processed. Mode `0` processes queries based on the title only, while mode `1` uses both the title and description of queries.
- **Query Processing and Retrieval**: If helper files are present, it loads the queries, stop words, inverted index, and maximum frequency dictionary to run the queries. If the helper files are not present, it calls `intializeHelper()` to create these files by processing the corpus, creating the vocabulary, document tokens, index, and other necessary data structures.
- **Making Results File**: The `makesResultsFile` function runs the queries against the indexed documents using the selected mode, stop words, the inverted index, and the maximum frequency dictionary. The results are then formatted and saved to `Results.txt`.
- **Helper Functions**: Includes `intializeHelper` for initializing and creating necessary files and data structures for the IR system, and `printResults` for formatting and outputting the retrieval results.


##### `distilbert.py` 

Utilizes ***DistilBERT***, a lightweight version of **BERT** that retains most of its performance on various NLP tasks. It is used for generating embeddings that are then leveraged for re-ranking. While emulating the processing functions of `cosine.py`, some its key functionalities include:  

- **Document and Query Encoding**: Utilizes ***DistilBERT*** to encode both document text and query text into dense vector representations. This process transforms the textual information into a format that captures semantic meaning, facilitating a deeper understanding of the content beyond mere keywords.
- **Multiprocessing for Efficiency**: Implements multiprocessing to handle the computationally intensive task of encoding documents and queries with ***DistilBERT***. This approach allows for parallel processing, significantly speeding up the encoding process across multiple CPU cores.
- **Cosine Similarity for Re-ranking**: After initial retrieval, it computes cosine similarity between the DistilBERT-encoded query vector and the encoded vectors of documents in the top results. This step ensures that documents are re-ranked based on semantic similarity, potentially improving the relevance of the results.
- **Result Integration and Output**: The re-ranked documents, based on their similarity to the query, are then prepared for presentation. This module leverages existing functionalities to format and output the final ranked list of documents.


##### `universal.py`

Employs the Universal Sentence Encoder for generating embeddings. This model is designed for a wide range of tasks and is known for producing high-quality embeddings for sentences and paragraphs. It also offers a different approach to encoding and similarity measurement compared to ***DistilBERT***, providing an alternative method for semantic matching. Key functionalities include:

- **Encoding with a Focus on Semantics**: Encodes queries and documents using the Universal Sentence Encoder, which is particularly well-suited for tasks requiring understanding of sentence-level semantics. This process generates embeddings that capture the essence of the text content.
- **Efficient Handling of Query and Document Vectors**: Processes embeddings to facilitate efficient comparison. Given the model's output, it organizes the data to enable straightforward computation of similarity scores between queries and documents.
- **Semantic Re-ranking Based on Embeddings**: Uses the embeddings to perform semantic re-ranking of documents. By calculating cosine similarity between query vectors and document vectors, it ensures that documents semantically related to the query are prioritized in the results.
- **Adaptability to Different Query Types**: Allows for flexibility in handling queries, supporting modes that consider either the title or a combination of the title and description. This adaptability ensures that the encoding process aligns with the specific informational intent behind each query.

## Explanation of Algorithms, Data Structures and Optimizations
---
The Information Retrieval (IR) system implemented in the project utilizes a variety of algorithms, data structures, and optimizations to facilitate efficient document processing, indexing, retrieval, and ranking, as well as adopting the mechanisms of advanced neural retrieval models. These elements combined contribute to an IR system that is capable of handling complex queries over large document collections with speed and accuracy. The use of efficient data structures and algorithms, coupled with targeted optimizations, ensures that the system can deliver relevant search results in a timely manner, demonstrating a thoughtful balance between computational efficiency and retrieval effectiveness. This thoughtful integration not only enhances the system's performance but also ensures it remains scalable and adaptable to evolving data and user needs.

### Preprocessing algorithms
---
- **Tokenization and Normalization**: Breaks and splits text into individual terms and normalizes them (e.g., lowercasing). This is fundamental for creating a consistent representation of text data.
- **Stop word Removal**: Excludes common words that offer little value in distinguishing document relevance. This reduces noise in the indexing and retrieval processes. While removing commonly used words, it is optimizing the query and document processing by focusing on significant terms.
- **Stemming**: Reduces words to their root form using the Porter Stemming algorithm. This helps in consolidating different forms of a word to a single index entry, by ensuring variations of a word are treated similarly, thus enhancing the system's ability to match queries to relevant documents.

### Indexing algorithms
---
- **Inverted Index Construction**: Utilizes an algorithm to map each term in the vocabulary to a list of documents in which that term appears. This structure is crucial for efficient retrieval, as it allows for rapid lookups of documents relevant to a query term.

### Retrieval and Ranking algorithms
---
- **Vector Space Model (VSM)**: Represents documents and queries as vectors in a multidimensional space, where the relevance is computed using cosine similarity. This algorithm is pivotal for ranking documents based on their relevance to a query.
- **TF-IDF Weighting**: Calculates term frequency-inverse document frequency (TF-IDF) scores to weight the importance of terms within documents and across the corpus. This algorithm enhances the discrimination of term relevance, improving the precision of document ranking.

### Semantic Embedding with Neural Models
---
- **DistilBERT and Universal Sentence Encoder**: Converts text to dense vector representations capturing deep semantic meanings, enabling the system to perform relevance matching based on conceptual similarity beyond mere keyword overlap.
- **Relevance Scoring and Ranking with Cosine Similarity**: Measures the cosine of the angle between document and query vectors as a proxy for their semantic similarity, providing a basis for ranking documents in order of relevance to the query.

## Data Structures
---
- **Inverted Index**:
	- A fundamental data structure in IR, mapping terms to the documents they appear in, facilitating efficient document retrieval by query terms. Optimized through JSON storage for rapid loading and access.
	
- **Sets and Lists**:
	- Used for storing tokens, stop words, and the vocabulary; Sets are utilized for storing unique tokens, aiding in the creation of the vocabulary and ensuring efficient processing of text data. Lists hold ordered collections of tokens and documents, useful in various processing stages, including tokenization and relevance scoring.
	
- **Dictionaries and Hash Tables**:
	- **Inverted Index**: A dictionary maps terms to their document lists, facilitating quick document retrieval for given terms.
	- **Document Frequency and Term Frequency Stores**: Used extensively for storing the vocabulary, document frequencies, term frequencies, and other critical information, enabling quick lookups that are essential for the processing and scoring phases.
	
- **JSON Files**:
	- Used to persist inverted indexes, term frequencies, and other metadata on disk. This format allows for structured storage and easy retrieval of preprocessing and indexing results.
	
- **Queues**:
	- Employed in multiprocessing tasks, especially in encoding document and query text with neural models, facilitating efficient task distribution among multiple processes.


## Optimizations
---

- **Preprocessing**:
	- **Efficient Stop word Removal**: By utilizing a set data structure for stop words, the preprocessing algorithm can quickly determine if a token is a stop word in constant time {_O(1)_}. This significantly speeds up the process of filtering out stop words from documents and queries.
    - **Streamlined Text Normalization**: The preprocessing steps likely apply text normalization (such as lowercasing and punctuation removal) in a single pass. This approach minimizes the number of times the text is iterated over, reducing computational overhead.
    
- **Indexing**:
    - **Batch Processing for Inverted Index Construction**: When constructing the inverted index, the algorithm processes documents in batches. This approach reduces memory usage by avoiding the need to load the entire document collection into memory at once.
    - **Use of Counter Objects for Term Frequency Calculation**: The Python `Counter` class from the `collections` package is used for efficiently counting the occurrence of terms in documents. This allows for rapid calculation of term frequencies (TF) during indexing, which is crucial for the subsequent calculation of TF-IDF scores.
    
- **Retrieval and Ranking**:
    - **Cosine Similarity Calculation Efficiency**: For calculating cosine similarity between document and query vectors, the algorithm only considers terms that appear in both the query and the document. This reduces the dimensionality of the vectors involved in the calculation, leading to faster similarity computations.
    - **Selective Document Loading**: When retrieving documents based on query terms, the system only loads document information that is necessary for ranking (e.g., term frequencies, document lengths) rather than the full document text. This significantly decreases the amount of data processed during retrieval.
    - **Early Termination in Ranking**: In the ranking process, an early termination strategy is employed, where documents are sorted by their potential relevance (e.g., based on the number of query terms they contain) and the system stops considering documents beyond a certain threshold. This reduces the number of documents that need to be fully evaluated for relevance.
    
- **Multiprocessing for Encoding**:
    - Parallelizes the computationally intensive task of generating semantic embeddings for documents and queries, significantly reducing processing time and enhancing system responsiveness.
    
- **Precomputed Embeddings and Stored Indexes**:
    - By precomputing and storing embeddings for documents, as well as maintaining serialized inverted indexes and other essential data structures, the system minimizes on-the-fly computation, leading to faster query processing and retrieval.
    
- **Selective Query Expansion**:
    - The system's capability to switch between using titles only or titles with descriptions for queries allows for dynamic adjustment based on the nature of the query or user preference, optimizing retrieval effectiveness.
    
- **Efficient Text Preprocessing**:
    - Implementations of tokenization, stop word removal, and stemming are optimized for speed and memory usage, ensuring that the preprocessing phase does not become a bottleneck.
    
- **General**:
	- **Caching**: While not explicitly mentioned, caching mechanisms can be implied in various stages of the IR system (e.g., caching the results of frequent queries or intermediate preprocessing steps). This can drastically reduce computation times for repetitive operations.
	- **Data Structure Choices**: The choice of data structures (e.g., dictionaries for the inverted index, sets for stop words) is inherently an optimization, as these structures are chosen for their efficiency in specific operations required by the IR system.


## Discussion of Results
---
The provided outputs from `trec_eval` give us an insight into how the Information Retrieval (IR) system implemented performs against the set of queries and the ideal query relevancies. With the augmentation of neural models, a comparison with the original IR system is made to evaluate superiority in performance. The commands used to run the `trec_eval` script for the IR system is the following (**`trec_eval` must be installed on the machine beforehand**):

This outputs overall assessment:

```bash

trec_eval ideal.txt Results.txt

```


And this outputs the MAP scores for each query:

```bash

trec_eval -q -m map ideal.txt Results.txt

```
  

The performance of the IR system is evaluated using `trec_eval`, focusing on the Mean Average Precision (MAP) score, a standard metric for evaluating the precision of retrieval systems across all levels of recall:
- The MAP score essentially averages the precision scores at the ranks where relevant documents are retrieved, offering a comprehensive measure of retrieval effectiveness.
- *R-precision* is the precision after retrieving R documents, where R is the number of relevant documents for a query. It is a single-value measure that represents how many of the first R retrieved documents are relevant.
- *Precision at Recall Levels (`P@R=level`)* measures the precision achieved after retrieving a certain percentage of the total relevant documents. It is a detailed metric that provides insights at various points of the recall curve.

The `trec_eval` scores provided from evaluating the IR system using `ideal.txt` (relevance judgments) and `Results.txt` (system rankings) reveal the following observations:

###### DistilBERT Performance:
- **MAP Score for Title Only (`mode = 0`)**: The MAP score for queries based only on the title tag is `0.2883`. This indicates a moderate level of retrieval effectiveness when using titles alone, showcasing ***DistilBERT's*** capability to capture semantic nuances even with limited context.
- **MAP Score for Title and Description (`mode = 1`)**: The MAP score slightly increases to `0.2897` when both titles and descriptions are used. The minimal increase suggests that ***DistilBERT's*** semantic understanding benefits from the additional context provided by descriptions, though the marginal improvement points to the model's already strong performance with concise titles.
- **R-precision (`Rprec`)**: `0.3240` and `0.3065` for modes `0` and `1`, indicating that, on average, around 32.4% of the first R retrieved documents (where R equals the total number of relevant documents) are relevant, while the slightly lower at score suggests that adding descriptions might slightly disperse the concentration of relevant documents in the top R positions.
- **Precision at different levels of retrieved documents (P_5, P_10, etc.)** shows a gradual decline from `0.7215` at `0%` recall to `0.0272` at `100%` recall. This pattern is typical, as achieving higher recall often involves retrieving more non-relevant documents, thereby reducing precision. A similar trend with a slight superior start at `0.7458` at `0%` recall, indicating that additional description slightly improves initial retrieval but ends similarly at `0.0284` at `100%` recall.

| Precision Level (mode 0) | Score  | Precision Level (mode 1) | Score  |
| ------------------------ | ------ | ------------------------ | ------ |
| P_5                      | 0.5000 | P_5                      | 0.4880 |
| P_10                     | 0.4440 | P_10                     | 0.4440 |
| P_15                     | 0.4093 | P_15                     | 0.3880 |
| P_20                     | 0.3780 | P_20                     | 0.3620 |
| P_30                     | 0.3360 | P_30                     | 0.3040 |
| P_100                    | 0.1782 | P_100                    | 0.1716 |
| P_200                    | 0.1063 | P_200                    | 0.1096 |
| P_500                    | 0.0502 | P_500                    | 0.0536 |
| P_1000                   | 0.0270 | P_1000                   | 0.0292 |

###### Universal Sentence Encoder Performance:
- **MAP Score for Title Only (`mode = 0`)**: Using the Universal Sentence Encoder, the MAP score for title-only queries is `0.2478`. This score, while respectable, is lower than that achieved with ***DistilBERT***, indicating differences in how each model processes and understands the semantic content of titles.
- **MAP Score for Title and Description (`mode = 1`)**: The MAP score improves to `0.2728` when including both titles and descriptions. This more substantial increase compared to DistilBERT underscores the Universal Sentence Encoder's ability to leverage additional textual context to enhance semantic matching.
- **R-precision (`Rprec`)**: `0.2798` and `0.2966` for modes `0` and `1`, where for titles only, it achieved lower than ***DistilBERT***, indicating a reduced effectiveness in placing relevant documents within the top R positions. Although the other mode shows a slight improvement to when descriptions are added, implying that additional context helps but still trails behind ***DistilBERT***.
- **Precision at different levels of retrieved documents (P_5, P_10, etc.)** starts at `0.6477` at `0%` recall, lower than ***DistilBERT***, reflecting its overall lower performance in aligning retrieved documents with relevancy, especially in the initial stages of recall. While for the titles and descriptions test, it begins at `0.7008` at `0%` recall, showing that additional context from descriptions does aid in improving precision in the initial retrieval phases, though it follows a similar declining trend to `0.0376` at `100%` recall.

| Precision Level (mode 0) | Score  | Precision Level (mode 1) | Score  |
| ------------------------ | ------ | ------------------------ | ------ |
| P_5                      | 0.3880 | P_5                      | 0.4200 |
| P_10                     | 0.3580 | P_10                     | 0.3780 |
| P_15                     | 0.3373 | P_15                     | 0.3587 |
| P_20                     | 0.3210 | P_20                     | 0.3380 |
| P_30                     | 0.2907 | P_30                     | 0.3027 |
| P_100                    | 0.1666 | P_100                    | 0.1752 |
| P_200                    | 0.1043 | P_200                    | 0.1145 |
| P_500                    | 0.0503 | P_500                    | 0.0546 |
| P_1000                   | 0.0270 | P_1000                   | 0.0292 |

###### Performance Insights
- **Impact of Query Expansion**: The inclusion of descriptions alongside titles generally improves MAP scores for both models, validating the hypothesis that additional context can enhance the model's understanding and retrieval performance. However, the degree of improvement varies, suggesting that the effectiveness of query expansion may depend on the specific characteristics and capabilities of the neural model used. Same pattern of improvement for precision at lower recall levels, indicating that more context leads to more accurate early retrievals. However, this benefit seems to taper off at higher recall levels.
- **Model-Specific Performance & Comparison**: ***DistilBERT*** consistently outperforms the ***Universal Sentence Encoder*** in this setup, albeit by a narrow margin in scenarios where both titles and descriptions are used. This could be attributed to ***DistilBERT's*** architecture and training, which might provide it with an edge in extracting and utilizing semantic signals from the text. With respect *R-precision* and *P@R_level*, ***DistilBERT*** consistently shows higher R-precision and precision at recall levels compared to the ***Universal Sentence Encoder***, suggesting it may be better at capturing and utilizing the semantic nuances of queries and documents.
- **Variability Across Queries**: The detailed MAP scores for individual queries reveal significant variability in performance across different queries. This suggests that certain types of queries or topics may be more challenging for the models, pointing to areas where further tuning or alternative approaches might be beneficial. Due to the **Precision-Recall Trade-off**, the decline in precision as recall increases underscores the inherent trade-off between retrieving all relevant documents (high recall) and ensuring those retrieved are indeed relevant (high precision). This highlights the challenge of balancing these objectives in IR systems.


To exemplify the findings, queries 3 and 20 are delved in deeper to understand the MAP scores associated with them;

###### Query 3:

- **Title**: Insurance Coverage which pays for Long Term Care

- **Description**: Document discusses insurance coverage for long term care confinements.

- **Narrative**: The relevant document discusses an existing or proposed insurance plan (governmental, commercial or individual) and the coverage it provides for long term care confinements in an institution or home care.

- **MAP Score - Title only (`mode = 0`) - DistilBERT**: `0.1553`

- Top 10 Ranking

```plaintext
3 Q0 AP880419-0133 1 0.6203454295173052 r1
3 Q0 AP880628-0074 2 0.48802257278433286 r1
3 Q0 AP880920-0017 3 0.47950333241735466 r1
3 Q0 AP880423-0088 4 0.4770005084480506 r1
3 Q0 AP880629-0212 5 0.474506216175808 r1
3 Q0 AP880526-0030 6 0.45996513152684076 r1
3 Q0 AP880320-0105 7 0.43895600164066584 r1
3 Q0 AP880430-0167 8 0.43351303177047895 r1
3 Q0 AP880518-0053 9 0.43074233487725117 r1
3 Q0 AP880620-0158 10 0.4304240160884501 r1
```

- **MAP Score - Title and Description (`mode = 1`) - DistilBERT**: `0.1122`

- Top 10 Ranking

```plaintext
3 Q0 AP880419-0133 1 0.4704479216383612 r2
3 Q0 AP880920-0017 2 0.4301793774405999 r2
3 Q0 AP880628-0074 3 0.42275714385015634 r2
3 Q0 AP880629-0212 4 0.39206704679180215 r2
3 Q0 AP880218-0044 5 0.39008206314510707 r2
3 Q0 AP880310-0025 6 0.37980830494832574 r2
3 Q0 AP880423-0088 7 0.37255418455063344 r2
3 Q0 AP880414-0118 8 0.3568159026952633 r2
3 Q0 AP880606-0154 9 0.3394543379091616 r2
3 Q0 AP880423-0086 10 0.3394019922593421 r2
```


- **MAP Score - Title only (`mode = 0`) - Universal Sentence Encoder: `0.3858`

- Top 10 Ranking

```plaintext
3 Q0 AP880609-0025 1 0.42488927949304367 r1
3 Q0 AP880701-0160 2 0.424642073460664 r1
3 Q0 AP880419-0133 3 0.4062123920845551 r1
3 Q0 AP881102-0086 4 0.38829784719377225 r1
3 Q0 AP880609-0027 5 0.38063408785975883 r1
3 Q0 AP880518-0053 6 0.37603189239375256 r1
3 Q0 AP880526-0030 7 0.3737957625968652 r1
3 Q0 AP880603-0052 8 0.3683771043037144 r1
3 Q0 AP881102-0317 9 0.3615198123776727 r1
3 Q0 AP880423-0086 10 0.3526777450225439 r1
```


- **MAP Score - Title and Description (`mode = 1`) - Universal Sentence Encoder: `0.3494`

- Top 10 Ranking

```plaintext
3 Q0 AP880419-0133 1 0.4384434949800484 r2
3 Q0 AP881102-0086 2 0.42886288469320316 r2
3 Q0 AP880609-0025 3 0.42825803849019745 r2
3 Q0 AP880701-0160 4 0.4261865476831424 r2
3 Q0 AP880518-0053 5 0.41629723071008495 r2
3 Q0 AP880609-0027 6 0.4011721972497795 r2
3 Q0 AP881102-0317 7 0.3919842284151993 r2
3 Q0 AP880526-0030 8 0.37146027017302286 r2
3 Q0 AP880525-0252 9 0.3683404939156758 r2
3 Q0 AP880513-0106 10 0.3679819658087901 r2
```

The drop in MAP score from mode 0 to mode 1 across both models suggests that the additional details provided by the description and narrative might have introduced specificity that wasn't as well-matched by the retrieved documents. This could indicate that the broader, more general query in the title alone was sufficient for retrieving relevant documents, and the extra specificity might have narrowed the search too much or introduced complexity that affected retrieval negatively.
  
###### Query 25:

- **Title**: The Consequences of Implantation of Silicone Gel Breast Devices 

- **Description**: the use of silicone gel breast implants manufactured by Dow-Corning Corporation and recipient's concerns regarding future medical problems that may occur as a result of manufacturing defects or lack of proper testing before approval for general public use.

- **Narrative**: Relevant documents provide pertinent data on the risks associated with silicone gel breast implants, including identified residual effects, emphasizing concerns about medical problems due to manufacturing defects or improper testing, risks associated with the implants, statements by the FDA, and litigation against Dow-Corning Corporation.

- **MAP Score - Title only (`mode=0`) - DistilBERT**: `0.7556`

- Top 10 Ranking

```plaintext
20 Q0 AP881111-0092 1 0.7436961456528991 r1
20 Q0 AP881122-0171 2 0.7179207044127985 r1
20 Q0 AP881123-0037 3 0.6862621841783193 r1
20 Q0 AP880627-0239 4 0.6860097377895901 r1
20 Q0 AP881110-0035 5 0.6611725424312208 r1
20 Q0 AP880406-0143 6 0.4478157378252557 r1
20 Q0 AP881121-0243 7 0.41251637451042567 r1
20 Q0 AP880613-0259 8 0.4077503482694126 r1
20 Q0 AP881110-0224 9 0.39113393909145205 r1
20 Q0 AP881111-0107 10 0.387298707187489 r1
```


- **MAP Score - Title and Description (`mode = 1`) - DistilBERT**: `0.6389`

- Top 10 Ranking

```plaintext
20 Q0 AP881122-0171 1 0.7731941920241808 r2
20 Q0 AP881111-0092 2 0.7276574994481317 r2
20 Q0 AP881123-0037 3 0.7076322561192967 r2
20 Q0 AP881110-0035 4 0.6958044388017725 r2
20 Q0 AP880627-0239 5 0.6084177539179872 r2
20 Q0 AP881121-0243 6 0.4678786514032555 r2
20 Q0 AP881103-0013 7 0.4249428876853216 r2
20 Q0 AP880406-0143 8 0.41767944501650955 r2
20 Q0 AP881022-0012 9 0.39818727915546026 r2
20 Q0 AP880705-0255 10 0.39365257219134303 r2
```


- **MAP Score - Title only (`mode = 0`) - Universal Sentence Encoder: `0.8056`

- Top 10 Ranking

```plaintext
20 Q0 AP881111-0092 1 0.3886502680945813 r1
20 Q0 AP881122-0171 2 0.36636686971530413 r1
20 Q0 AP881123-0037 3 0.35572675558241873 r1
20 Q0 AP881110-0035 4 0.3317825207986624 r1
20 Q0 AP880406-0143 5 0.2306234337581247 r1
20 Q0 AP881104-0086 6 0.22550576018865234 r1
20 Q0 AP880929-0059 7 0.20602534598138045 r1
20 Q0 AP880610-0012 8 0.2056216488191005 r1
20 Q0 AP880627-0239 9 0.19505562397021703 r1
20 Q0 AP880324-0251 10 0.18542189556872765 r1
```


- **MAP Score - Title and Description (`mode = 1`) - Universal Sentence Encoder: `0.6389`

- Top 10 Ranking

```plaintext
20 Q0 AP881122-0171 1 0.6008209950167985 r2
20 Q0 AP881111-0092 2 0.5986741171465565 r2
20 Q0 AP881123-0037 3 0.5780181802797002 r2
20 Q0 AP881110-0035 4 0.5777028624810175 r2
20 Q0 AP880616-0020 5 0.42889784403847697 r2
20 Q0 AP880627-0239 6 0.40997727860364264 r2
20 Q0 AP881110-0224 7 0.39710783612134765 r2
20 Q0 AP880416-0007 8 0.3966962263405016 r2
20 Q0 AP881121-0243 9 0.38618964509507475 r2
20 Q0 AP880224-0220 10 0.37881018657779464 r2
```

The high MAP score for mode 0, particularly for the Universal Sentence Encoder, suggests that the specific and targeted nature of the title was very effective on its own for guiding the retrieval of highly relevant documents. The decrease in MAP score for mode 1, while still remaining relatively high, indicates that the additional context provided by the description and narrative might have introduced details that, although relevant, could have complicated the retrieval process by adding numerous specific conditions for relevance. The specificity and complexity of the additional information might have made it more challenging for the models to match documents precisely to the query criteria.


Given these results for queries 3 and 20, the effectiveness of mode 1 (title and description) versus mode 0 (title only) appears to be influenced by how the additional information in the description and narrative aligns with the document set's content. For Query 3, the added complexity reduced retrieval precision, while for Query 20, the specific details provided context that was beneficial but slightly less effective than using the title alone. These observations underline the nuanced impact that query formulation and additional context can have on the performance of neural models in IR systems. It highlights the importance of balancing specificity and breadth in query construction to optimize retrieval performance. To summarize the results from all models, the ***DistilBERT*** model performed best, with the mode of `1` regarding the MAP score, whereas its counterpart of mode `0` performed the best in terms of R-Precision (see the `results` folder for results of all neural models, as well as the `trec_eval` scores for both parts of the project assignment):

| Model      | Mode | MAP Score | R-Precision |
| ---------- | ---- | --------- | ----------- |
| Distilbert | 0    | 0.2883    | 0.3240      |
| Distilbert | 1    | 0.2897    | 0.3065      |
| Universal  | 0    | 0.2478    | 0.2798      |
| Universal  | 1    | 0.2728    | 0.2966      |
| IR_A1      | 0    | 0.1677    | 0.1820      |
| IR_A1      | 1    | 0.2273    | 0.2353      |

All in all, the MAP score is **inferior** when title and description provides a larger vocabulary in comparison to the first part of the project assignment which raises the notion that this analysis demonstrates the critical role of query specificity and the added value (or potential challenges) of incorporating detailed descriptions in affecting the neural model-based IR system's ability to accurately retrieve and rank documents. The performance trend suggests that the effectiveness of including descriptions varies depending on the nature of the query. For specific, well-defined queries, additional description may not always enhance and can sometimes detract from retrieval performance. Query specificity and the alignment of query terms with document content play significant roles in determining the benefits of query expansion through descriptions. These results underscore the importance of carefully considering the characteristics of each query when deciding on the use of titles alone or in conjunction with descriptions for document retrieval. The effectiveness of these approaches can significantly vary depending on how they align with or diverge from the content and focus of the relevant documents.


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

Improving an Information Retrieval (IR) system, especially one augmented by neural models, involves a multifaceted approach. Considering the complexity and the evolving nature of both information needs and technological advancements, here are several areas for future work aimed at enhancing your IR system's performance:

 1. **Exploration of Advanced Neural Models**
- **Experiment with Newer Language Models**: Beyond ***DistilBERT*** and ***Universal Sentence Encoder***, can explore the latest models such as ***GPT-3***, ***RoBERTa***, or ***BERT-large***. These models may offer improved understanding of complex queries and documents due to their larger training datasets and advanced architectures.
- **Domain-specific Fine-tuning**: Custom fine-tuning of pre-trained models on a domain-specific corpus can significantly enhance model relevance to the specific information retrieval context, improving accuracy and effectiveness.
- **Multilingual and Cross-lingual Models**: To accommodate diverse user bases, incorporating multilingual models or cross-lingual embedding techniques can expand the system's applicability across different languages and cultures.

2. **Enhanced Query Understanding**
- **Query Intent Classification**: Implementing machine learning models to classify query intent (informational, navigational, transactional) could enable more targeted retrieval strategies tailored to the user's actual needs.
- **Semantic Query Expansion**: Utilizing semantic networks or knowledge graphs for query expansion can enrich queries with related concepts, synonyms, or entities, potentially uncovering documents that are relevant but might not explicitly match the query terms.

 3. **Relevance Feedback and Interactive Search**
- **Incorporate User Feedback**: Implementing relevance feedback mechanisms where users can indicate the relevance of retrieved documents can help refine and improve search results over time.
- **Interactive Search Interfaces**: Developing interactive search interfaces that allow users to refine their queries, filter results, or explore related topics could enhance user engagement and satisfaction.

 4. **Personalization and Contextualization**
- **User Profile Building**: Creating dynamic user profiles based on historical search behavior and interactions can enable personalized search experiences, tailoring results to individual preferences or informational needs.
- **Context-aware Retrieval**: Integrating context-aware algorithms that consider the user's current environment, time, device, or previous queries can provide more relevant and situational search results.

 5. **Optimization and Scalability**
- **Indexing Optimization**: Experimenting with different indexing structures or compression techniques can improve the speed and efficiency of document retrieval.
- **Scalable Vector Search**: Leveraging scalable vector search engines like FAISS or Annoy for efficient similarity search in high-dimensional spaces can enhance the performance of neural model-based retrieval.

 6. **Evaluation and Benchmarks**
- **Extended Evaluation Metrics**: Beyond traditional metrics like MAP or R-precision, incorporating user-centric evaluation metrics such as user satisfaction, task completion time, or click-through rates can provide more holistic insights into system performance.
- **Continuous Benchmarking**: Establishing continuous benchmarking processes against evolving datasets and queries can ensure the system remains effective and relevant to current information needs.

 7. **Integration of Multimodal Data**
- **Multimodal Search Capabilities**: Extending the IR system to handle and retrieve multimodal data (images, videos, audio) alongside textual information can address a broader range of user queries and preferences.
- **Semantic Embeddings for Multimodal Data**: Researching and implementing semantic embedding techniques that work across different data types can unify the retrieval process, offering comprehensive results that span various content formats.