import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.4pk5c.mongodb.net/?retryWrites=true&w=majority")
# client = pymongo.MongoClient("mongodb://test:mongodb@cluster0-shard-00-00.vye4g.mongodb.net:27017,cluster0-shard-00-01.vye4g.mongodb.net:27017,cluster0-shard-00-02.vye4g.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-9d2upr-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"sudhanshu",
    "email":"sud@gmail.com",
    "surname":"kumar"}
db1=client['mongotest']
col1=db1['test']
col1.insert_one(d)