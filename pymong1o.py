from pymongo import MongoClient
from datetime import datetime

# Establish a connection to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Access the desired database and collection
db = client["your_database_name"]
collection = db["your_collection_name"]

# Define the range of "created_at" values in ISO format
start_date = "2022-01-01T00:00:00Z"  # Define your start date
end_date = "2022-12-31T23:59:59Z"  # Define your end date

# Construct the query using ISO format dates
query = {
    "created_at": {
        "$gte": start_date,
        "$lte": end_date
    }
}

# Execute the query
results = collection.find(query)

# Process the results
for document in results:
    print(document)

# Close the MongoDB connection
client.close()
