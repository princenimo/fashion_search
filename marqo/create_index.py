from marqo import Client
import config

# Set up Marqo client for local Docker instance
# Make sure you have Marqo running on http://localhost:8882
mq = Client(url="http://localhost:8882")

# Define Marqo index name
index_name = config.INDEX_NAME

# Define the index settings
settings = {
    "treatUrlsAndPointersAsImages": True,  # Indicates that URLs or pointers in the data should be treated as image inputs
    "model": "ViT-B/32",  # Specifies the embedding model to be used for indexing and querying
}

# Create the index
mq.create_index(index_name = index_name, settings_dict=settings)