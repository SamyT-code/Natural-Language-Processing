# Take the queries in queries.txt and make an object of 4 attributes (num, title, desc, and narr). 
# Put all these objects in a hash table

class Query:
    def __init__(self):
        self.num = None
        self.title = None
        self.desc = None
        self.narr = None

def read_queries(file_path):
    queries = []
    current_query = None
    current_desc_lines = []
    current_narr_lines = []
    state = None  # Possible states: None, 'desc', 'narr'

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("<top>"):
                current_query = Query()
            elif line.startswith("<num>"):
                current_query.num = int(line.lstrip("<num>").strip())
            elif line.startswith("<title>"):
                current_query.title = line.lstrip("<title>").strip()
            elif line.startswith("<desc>"):
                current_desc_lines = []
                state = 'desc'
            elif line.startswith("<narr>"):
                current_narr_lines = []
                state = 'narr'
            elif line.startswith("</top>"):
                current_query.desc = " ".join(current_desc_lines).strip()
                current_query.narr = " ".join(current_narr_lines).strip()
                queries.append(current_query)
                state = None

            # Accumulate lines for description and narrative based on state
            if state == 'desc' and not line.startswith("<"):
                current_desc_lines.append(line)
            elif state == 'narr' and not line.startswith("<"):
                current_narr_lines.append(line)

    return queries

def create_hash_table(queries):
    hash_table = {}
    for query in queries:
        hash_table[query.num] = query
    return hash_table

# Read queries from the file
file_path = 'queries.txt'  # Assuming 'queries.txt' is in the same directory
queries = read_queries(file_path)

# Create a hash table with the queries
hash_table = create_hash_table(queries)

# Accessing an example query from the hash table (e.g., Query with num=2)
example_query_num = 1
example_query = hash_table.get(example_query_num)

# Printing the information of the example query
if example_query:
    print(f"EXAMPLE QUERY {example_query.num}: \n")
    print(f"Title: {example_query.title} \n")
    print(f"Description: {example_query.desc} \n")
    print(f"Narrative: {example_query.narr} \n")
else:
    print(f"Query with number {example_query_num} not found.")
