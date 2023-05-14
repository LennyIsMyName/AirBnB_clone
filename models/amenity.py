from models.base_model import BaseModel
""" clsaa Amenity """

class Amenity(BaseModel):
    """ name of the amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
