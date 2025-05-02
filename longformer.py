# The format is just like BERT
# pip install transformers

import re
import os
import logging
from transformers import LongformerTokenizer, LongformerModel
import multiprocessing
from multiprocessing import Manager, Queue
import queue  # For queue.Empty exception handling

# Initialize the Longformer model and tokenizer
tokenizer = LongformerTokenizer.from_pretrained('allenai/longformer-base-4096')
model = LongformerModel.from_pretrained('allenai/longformer-base-4096')

def processDoc(rawdocumenttext):
    # Extract document number and text from raw document text
    documentnumberpattern = re.compile(r"<DOCNO>(.*?)</DOCNO>")
    documentnumber = documentnumberpattern.findall(rawdocumenttext)[0].strip()

    documenttextpattern = re.compile(r"<TEXT>(.*?)</TEXT>", re.DOTALL)
    documenttext = " ".join(documenttextpattern.findall(rawdocumenttext)).replace('\n', " ").strip()

    return documentnumber, documenttext

def readFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def processFile(filetext, documentdictionary):
    pattern = re.compile(r'<DOC>(.*?)</DOC>', re.DOTALL)
    documents = pattern.findall(filetext)
    for document in documents:
        docnum, doctext = processDoc(document)
        documentdictionary[docnum] = doctext

def processCorpus(corpus_directory):
    documentdictionary = {}
    for entry in os.scandir(corpus_directory):
        if entry.is_file():
            filetext = readFile(entry.path)
            processFile(filetext, documentdictionary)
    return documentdictionary

def encode(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=4096, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

def encodeWorker(inqueue, outdict):
    while True:
        try:
            docnum, doctext = inqueue.get_nowait()
        except queue.Empty:
            break
        else:
            outdict[docnum] = encode(doctext)
            print(f"Encoded {docnum}")

def encodeDocuments(documentdictionary):
    encodeddictionary = {}
    inqueue = Queue()
    manager = Manager()
    outdict = manager.dict()

    for docnum, doctext in documentdictionary.items():
        inqueue.put((docnum, doctext))

    processes = [multiprocessing.Process(target=encodeWorker, args=(inqueue, outdict))
                 for _ in range(multiprocessing.cpu_count())]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    encodeddictionary.update(outdict)
    return encodeddictionary

def main():
    corpus_directory = 'coll/'  # Assuming the document collection is in the 'coll/' directory
    documentdictionary = processCorpus(corpus_directory)
    encodeddictionary = encodeDocuments(documentdictionary)

    # Here you could store the encoded dictionary or further process it
    print("Encoding complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
