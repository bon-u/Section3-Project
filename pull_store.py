import os
import csv
from pymongo import MongoClient

FILEPATH = os.path.join(os.getcwd(), 'healthcare-dataset-stroke-data.csv')
#파일 경로

FILE=open(FILEPATH,'r')
data=csv.DictReader(FILE)
#csv dict형태로 불러오기

HOST = 'cluster0.0eulv.mongodb.net'
USER = 'Treachery'
PASSWORD = '4345350'
DATABASE_NAME = 'myFirstDatabase'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=false&ssl_cert_reqs=CERT_NONE"
COLLECTION_NAME = 'strokedata'
#MONGODB URI

client=MongoClient(MONGO_URI)
database=client[DATABASE_NAME]
collection=database[COLLECTION_NAME]
for i in data:
    collection.insert_one(i)
#MONGODB 데이터 입력