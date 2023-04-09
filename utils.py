import json, datetime, bson
import pymongo

class CustomEncoder(json.JSONEncoder):
    """A C{json.JSONEncoder} subclass to encode documents that have fields of
    type C{bson.objectid.ObjectId}, C{datetime.datetime}
    """
    def default(self, obj):
        if isinstance(obj, bson.objectid.ObjectId):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
    
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        print(obj)
        if isinstance(obj, bson.objectid.ObjectId):
            return str(obj)
        elif isinstance(obj, Cursor):
            return list(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
