
from fastapi import FastAPI, HTTPException
from uuid import uuid4
import logging
from app.backend import app  # This is the backend app object itself, without REST API.
from app.backend.model.WorkItem import WorkItem
from app.backend.model.Progress import Progress
from app.backend.service.redis_store import RedisStore

# The initial version in the REST API URLs is "v0.1", since this is just a POC.

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s")
logger = logging.getLogger(__name__)

redis_store = RedisStore()


# SYSTEM METHODS

@app.get("/v0.1/~SYSTEM~/progress-values")
def get_valid_progress_values() -> list[int]:
    """
    Obtains the list of values permissible as points of progress of work in a WorkItem (e.g., 0, 25, 50, 75, 100).
    ["~sys~" is the piece of a REST URL that says this is a system method, not for general public use.
    This method is somewhat optional, just being one kind of design experiment to reduce code duplication and promote "one source of truth".
    The frontend can grab the valid points of progress allowed by the backend, so the frontend can enforce only valid values.]

    Returns:
        list[int]: The list of allowable progress points.
    """
    return [point.value for point in Progress]


# CREATE METHODS

@app.post("/v0.1/workitems/", response_model=dict[str, str])
def create_workitem(workitem: WorkItem) -> dict:
    """
    Creates a WorkItem in the store from the content of a supplied WorkItem.

    Args:
        workitem (WorkItem): The source of WorkItem content from which to create this new WorkItem.

    Raises:
        HTTPException: If creation fails.

    Returns:
        str: A message to the caller.
        WorkItem: The created WorkItem.
    """
    redis_store.create_workitem(workitem.id, workitem.model_dump())  # Returns True.
    logger.info(f"WorkItem: CREATED id {workitem.id} by user {workitem.user}")
    return
    {
        "message": f"WorkItem (id: {workitem.id}) was created successfully.",
        "workitem": workitem.model_dump()
    }


# READ METHODS

@app.get("/v0.1/workitems/{id}", response_model=dict[str, str])
def read_workitem(id: uuid4) -> dict:
    """
    Gets a specific WorkItem from the store using its id.

    Args:
        id (uuid4): The id representing the desired WorkItem.

    Raises:
        HTTPException: If reading fails.
        
    Returns:
        dict: The desired WorkItem.
    """
    workitem = redis_store.read_workitem(id)
    if not workitem:
        raise HTTPException(status_code=404, detail=f"The WorkItem (id: {id}) was not found.")
    logger.info(f"WorkItem: READ id {id}")
    return
    {
        "workitem": workitem
    }


# WRITE METHODS

@app.put("/v0.1/workitems/{id}", response_model=dict[str, str])
async def update_workitem(id: str, new_workitem: WorkItem) -> dict:
    """
    Updates a WorkItem in the store, returning the updated WorkItem to the caller..

    Args:
        id (str): The id uniquely identifying the WorkItem to update.
        new_workitem (WorkItem): The content of the new WorkItem to apply to this given WorkItem.

    Raises:
        HTTPException: If updating fails.
        
    Returns:
        dict: The updated object.
    """
    workitem = redis_store.update_workitem(id, new_workitem.model_dump())
    if not workitem:
        raise HTTPException(status_code=404, detail=f"WorkItem ({id}) was not found.")
    
    return
    {
        "message": "WorkItem (id: {workitem.id}) was updated successfully.",
        "workitem": workitem.model_dump()
    }


@app.delete("/v0.1/workitems/{id}", response_model=dict[str, str])
async def delete_workitem(id: str) -> dict:
    """
    Deletes a WorkItem from the store.

    Args:
        id (str): The id uniquely identifying the WorkItem to delete.

    Raises:
        HTTPException: If deleting fails.

    Returns:
        dict: _description_
    """
    if not redis_store.delete_workitem(id):
        raise HTTPException(status_code=404, detail=f"WorkItem ({id}) was not found.")
    return
    {
        "message": "WorkItem (id: {workitem.id}) was deleted successfully.",
    }
