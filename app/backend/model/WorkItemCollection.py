
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timezone
from uuid import uuid4  # uuid4 is a random UUID.
from app.backend.model.WorkItem import WorkItem



from typing import List, Dict
from uuid import uuid4
from app.backend.service.redis_store import RedisStore

class WorkItemCollection:
    """
    This class provides a representation of a plurality of WorkItems,
    i.e., methods that work with or return some collection of WorkItems.
    It is debatable that these methods could/should just go in the WorkItem class.
    These look like static/class utility methods, but in theory someone
    might want to use these methods with a different RedisStore, which
    would then need to be passed in as an argument.
    """
    def __init__(self, redis_store: RedisStore):
        self.redis_store = redis_store


    def get_all_workitems(self) -> list[dict]:
        """
        Reads all WorkItems available in the data store.
        Note: Missing WorkItem ids are skipped.

        Returns:
            list[dict]: The complete list of WorkItems, where each element is a WorkItem (dict).
        """
        result_workitems = []
        # All keys in redis. keys = WorkItem ids.
        for id in self.redis_store.client.keys("*"):
            workitem = self.redis_store.read_workitem(id)
            if workitem:
                result_workitems.append(workitem)
        return result_workitems
    

    def filter_workitems_by_user(self, user_id: str) -> list[dict]:
        """
        Retrieve all the WorkItems and ONLY those items that are assigned
        to the specified user id (which is a UUID).

        Args:
            user_id (str): The individual user id by which to select the desired WorkItems.

        Returns:
            list[dict]: The list of desired WorkItems according to the chosen user.
        """
        return [ workitem for workitem in self.get_all_workitems() if workitem.get("user") == user_id ]


