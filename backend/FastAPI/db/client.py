from pymongo import MongoClient 

# Base de datos local MongoDB (Docker container)
#db_client = MongoClient().local

# Base de datos remota MongoDB Atlas (descomentar cuando las credenciales sean correctas)
db_client = MongoClient(
    "mongodb+srv://alejandrojfs26_db_user:test@cluster0.wjuujns.mongodb.net/").test


#from pymongo import MongoClient
#from pymongo.server_api import ServerApi

#uri = "mongodb+srv://alejandrojfs26:6Hg6F61bgOyQsr6@cluster0.wjuujns.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
#try:
 #   client.admin.command('ping')
  #  print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
 #   print(e)