# Take the queries in queries.txt and make an object of 4 attributes (num, title, desc, and narr). 
# Put all these objects in a hash table

class Query:

    def __init__(self):
        self.num = None
        self.title = None
        self.desc = None
        self.narr = None

    @classmethod
    def read_queries(cls,file_path):
        queries = {}
        current_query = None
        state = None  # Possible states: None, 'desc', 'narr', 'title'

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith("<top>"):
                    current_query = Query()
                elif line.startswith("<num>"):
                    current_query.num = int(line.lstrip("<num>").strip())
                elif line.startswith("<title>"):
                    current_title_lines = []
                    state = "title"
                    current_title_lines.append(line.lstrip("<title>").strip())
                elif line.startswith("<desc>"):
                    current_desc_lines = []
                    state = 'desc'
                    current_desc_lines.append(line.lstrip("<desc>").strip())
                elif line.startswith("<narr>"):
                    current_narr_lines = []
                    state = 'narr'
                    current_narr_lines.append(line.lstrip("<narr>").strip())
                elif line.startswith("</top>"):
                    current_query.title = " ".join(current_title_lines).strip()
                    current_query.desc = " ".join(current_desc_lines).strip()
                    current_query.narr = " ".join(current_narr_lines).strip()
                    queries.update({current_query.num : current_query})
                    state = None

                # Accumulate lines for description and narrative based on state
                if state == 'desc' and not line.startswith("<"):
                    current_desc_lines.append(line)
                elif state == 'narr' and not line.startswith("<"):
                    current_narr_lines.append(line)
                elif state == 'title'and not line.startswith("<"):
                    current_title_lines.append(line)

        return queries

    



def create_hash_table(queries):
    hash_table = {}
    for query in queries:
        hash_table[query.num] = query
    return hash_table

# # Accessing an example query from the hash table (e.g., Query with num=2)
# example_query_num = 1
# example_query = hash_table.get(example_query_num)

# # Printing the information of the example query
# if example_query:
#     print(f"EXAMPLE QUERY {example_query.num}: \n")
#     print(f"Title: {example_query.title} \n")
#     print(f"Description: {example_query.desc} \n")
#     print(f"Narrative: {example_query.narr} \n")
# else:
#     print(f"Query with number {example_query_num} not found.")
