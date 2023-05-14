from models.base_model import BaseModel
import models

class User(BaseModel):
    """A class representing a user."""

    def __init__(self, *args, **kwargs):
        """Initializes a new User."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
