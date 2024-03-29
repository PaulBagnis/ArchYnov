from json import loads
from kafka import KafkaConsumer
from tools.mongo import MongodbClient
from datetime import datetime

print(" - Application started!")

MONGODB_CLIENT = MongodbClient()
CHECK_DUPLICATES = ['id', 'original_title']

# Create Kafka consumer
consumer = KafkaConsumer(
    "tmdb",
    bootstrap_servers=["kafka:29092"],
    api_version=(0, 10, 1),
)

for value in consumer:
    # on convertit les datas envoyer par le consumer bytes -> dict
    data = loads(value.value.decode("utf-8"))
    try:
        data["release_date"] = datetime.strptime(data["release_date"], '%Y-%m-%d')
        MONGODB_CLIENT.insertOne("tmdb", data, CHECK_DUPLICATES)
        print("insertion en base réussis")
    except:
        print("erreur lors de l'insertion en base")