from marqo import Client
import config

# Initialize Marqo client for local Docker instance
# Make sure you have Marqo running on http://localhost:8882
mq = Client(url="http://localhost:8882")

index_name = config.INDEX_NAME

# Get documents by their ID
res = mq.index(config.INDEX_NAME).get_document(
    document_id="71246356_0",
)

print(res)

# Delete documents by their ID
mq.index(index_name).delete_documents(
    ids=[
        "71246356_0",
        ]
    )