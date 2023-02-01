from pymongo import MongoClient

# A Completer
class MongodbClient():

    def __init__(self):
        self.client = MongoClient("mongodb://root:root@mongo:27017/")
        self.db = self.client["ydays"]

    def getCollection(self, name_collection):
        """get collection

        Args:
            name_collection (str): name of the collection

        Returns:
            collection: collection
        """

        collection = self.db[name_collection]
        collection = self.db.get_collection(name_collection)
        return collection
    
    def getAllDocumentsFromCollection(self, name_collection):
        """get all documents

        Args:
            name_collection (str): name of the collection

        Returns:
            collection: collection
        """
        
        collection = self.db[name_collection]
        allCollection = collection.find({})
        return allCollection
    

    def insertOne(self, name_collection, data):
        """insert un element en base de données

        Args:
            name_collection (str): Name of the collection
            data (dict): data insert in bdd
        """
        print("insert")
        collection = self.getCollection(name_collection)
        collection.insert_one(data)  