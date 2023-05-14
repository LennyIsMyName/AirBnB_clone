from models.base_model import BaseModel

""" class City """

class City(BaseModel):
    """ gives the state id and city name """
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
