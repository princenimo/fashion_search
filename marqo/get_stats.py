from marqo import Client
import config

# Initialize Marqo client for local Docker instance
# Make sure you have Marqo running on http://localhost:8882
mq = Client(url="http://localhost:8882")

# Define Marqo index name
index_name = config.INDEX_NAME

# Get index stats
res = mq.index(index_name).get_stats()

print(res)