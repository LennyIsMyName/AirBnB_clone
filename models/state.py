from models.base_model import BaseModel

""" State class """


class State(BaseModel):
    """ Gives the name of the state """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Init
        """
        super().__init__(*args, **kwargs)
