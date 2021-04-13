from pymongo import MongoClient
from collections import defaultdict

my_list = [
    {"id": 1, "name": "John"}
] 
my_list2 = [
    {"id": 2, "name": "Gadi"}
] 

class DatabaseClient:

    def __init__(self, port_number):
        self.client = MongoClient('localhost', port_number)
        self.db_dict = dict()
        self.db_coll = defaultdict(dict)

    def create_database(self, db_name):
        self.db_dict[db_name] = self.client[db_name]
        return self.db_dict[db_name]
    
    def create_collection(self, db_name, coll_name):
        self.db_coll[db_name][coll_name] = self.db_dict[db_name][coll_name]
        return self.db_coll[db_name][coll_name]

    def insert__to_collection(self, db_name, coll_name, data):
        query = {"id": int(data[0]["id"])}
        if(self.db_coll[db_name][coll_name].count_documents(query)>0):
            print("Query Already Exist")
            return -1
        self.db_coll[db_name][coll_name].insert_many(data)
        return 0


def main():
    client = DatabaseClient(27017)
    client.create_database("Elad")
    client.create_collection(db_name="Elad", coll_name="App")
    client.insert__to_collection("Elad", "App", my_list2)

if __name__ == "__main__":
    main()