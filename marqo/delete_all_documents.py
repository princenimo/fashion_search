from marqo import Client

# Initialize Marqo client for local Docker instance
# Make sure you have Marqo running on http://localhost:8882
mq = Client(url="http://localhost:8882")

# For safety reasons, replace this with your index name here
index_name = "your-index-name"

# This will delete all documents in your index
def empty_index(input_index_name):
    index = mq.index(input_index_name)
    res =  index.search(q = '', limit=400)
    while len(res['hits']) > 0:
        id_set = []
        for hit in res['hits']:
            id_set.append(hit['_id'])
        index.delete_documents(id_set)
        res = index.search(q = '', limit=400)

empty_index(index_name)
