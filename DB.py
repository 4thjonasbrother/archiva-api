from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import traceback


class ArchivaDB:
    def __init__(self):
        uri = "mongodb://10.12.29.68:27017/?directConnection=true"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.DhuvasDatabase = self.client["365"]
        self.RacksDatabase = self.client["racks"]
    
    def get_dhuvas(self):
        """Get all the items in 365 Dhuvas collection."""
        dhuvas = self.DhuvasDatabase["dhuvas"].find({})
        return [
            {
                "id": str(day["_id"]),
                "day" : day["day"],
                "month": day["month"],
                "year": day["year"],
                "detail": day["detail"],
                "source": day["source"] 
            } for day in dhuvas
        ]
    
    def add_dhuvas(self, day: int, month: int, year: int, detail: str, source: str):
        """Add an item (dhuvas) to 365 Dhuvas collection."""
        dhuvasCollection = self.DhuvasDatabase["dhuvas"]
        dhuvasCollection.insert_one({
            "day": day,
            "month": month,
            "year": year,
            "detail": detail,
            "source": source
        })
    
    def remove_dhuvas(self, dhuvasId: str):
        dhuvasCollection = self.DhuvasDatabase["dhuvas"]
        try:
            dhuvasCollection.delete_one({"_id": ObjectId(dhuvasId)})
            return True
        except Exception:
            print(traceback.print_exc())
            return False

    def get_racks(self):
        """Get the list of the records room racks."""
        racksCollection = self.RacksDatabase["racks"]
        return [rack for rack in racksCollection.find({})]


if __name__ == "__main__":
    db = ArchivaDB()
