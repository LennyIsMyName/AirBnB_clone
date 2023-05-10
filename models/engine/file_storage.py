import json
from datetime import datetime
from models.base_model import BaseModel

class DateTimeEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that can handle datetime objects
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return super().default(obj)

class FileStorage:
    """
        File Storage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all __object class
        """
        return self.__objects

    def new(self, obj):
        """
        adds object class to attribues.
        """
        dict_attrs = obj.to_dict()
        new_key = "{}.{}".format(dict_attrs["__class__"], dict_attrs["id"])
        self.__objects[new_key] = obj


    def save(self):
        """
        Serializes the __obj dict to a json file
        """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2, cls=DateTimeEncoder)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = {}
                if content != "":
                    try:
                        dict_from_file = json.loads(content)
                    except json.decoder.JSONDecodeError:
                        pass
                
                for file_key, dict_obj in dict_from_file.items():
                    if file_key not in FileStorage.__objects.keys():
                        className = dict_obj["__class__"]
                        newInst = eval("{}(**dict_obj)".format(className))
                        self.new(newInst)
        except FileNotFoundError:
            pass
