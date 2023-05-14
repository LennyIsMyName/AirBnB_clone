from models.base_model import BaseModel

""" class Review """

class Review(BaseModel):
    """ attributes of review """
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
