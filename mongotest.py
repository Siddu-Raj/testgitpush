import pymongo
from urllib.parse import quote_plus

# Correctly escape username and password
username = quote_plus("sidduraj872001")
password = quote_plus("Mongodb@872001")

# Construct the connection string
connection_string = f"mongodb+srv://{username}:{password}@cluster0.gptkr1r.mongodb.net/test?retryWrites=true&w=majority"

# Connect to MongoDB
client = pymongo.MongoClient(connection_string)
db = client.test

# Print the database object
print(db)
