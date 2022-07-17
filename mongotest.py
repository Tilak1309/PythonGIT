# import ssl
# ssl_cert_reqs=ssl.CERT_NONE
import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.4pk5c.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)

db = client.test
print(db)

d={
    "name":"sudhanshu",
    "email":"sud@gmail.com",
    "surname":"kumar"}
db1=client['mongotest']
col1=db1['test']
col1.insert_one(d)
