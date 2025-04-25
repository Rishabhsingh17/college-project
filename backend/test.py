from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URI = "mongodb+srv://Rishabh141:Rishabh17@db1.fkymhaz.mongodb.net/?retryWrites=true&w=majority&appName=db1"

try:
    # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection on a request as the
    print("✅ Successfully connected to MongoDB Atlas")

    # Choose database and collections
    db = client["campus_fix"]
    users_collection = db["users"]
    issues_collection = db["issues"]

    # Show document counts
    print(f"\n📦 'users' collection has {users_collection.count_documents({})} documents.")
    print(f"📦 'issues' collection has {issues_collection.count_documents({})} documents.")

    # Print documents if any
    def display_data(collection, name):
        print(f"\n🔍 Contents of '{name}' collection:")
        for doc in collection.find():
            print(doc)

    display_data(users_collection, "users")
    display_data(issues_collection, "issues")

except ConnectionFailure as e:
    print("❌ Failed to connect to MongoDB:", e)
except Exception as ex:
    print("⚠️ Error:", ex)
