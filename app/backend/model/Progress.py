
from pydantic import BaseModel

class Progress(BaseModel):
    """The range of possible values that progress can take.
    This is limited in this way, because progress will be manually specified by the user.
    Therefore, progress will be inexact, because we will not generally have a rigorous definition of "done"."""
    NONE = 0,
    ONE_FOURTH = 25,
    TWO_FOURTHS = 50,
    THREE_FOURTHS = 75,
    DONE = 100

