
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timezone, now
from uuid import uuid, uuid4
from app.backend.model.Progress import Progress


class WorkItem(BaseModel):
    """
    The model of the user's task, aka work item in the person's task board.

    Args:
        BaseModel (class): The base class required by pydantic to enable its feature.
    """

    id: uuid4  # This is a random UUID (aka GUID), which (as we all know) is a unique string (not an int) of form like this (case-insensitive): "123e4567-e89b-12d3-a456-426614174000".
    title: str
    description: str  # Details as to what this task is, the steps or requirements, etc. It can be updated/revised as the work is being done.
    depends_on: list[uuid4]  # Ids of WorkItem that this WorkItem depends directly on (possibly forming a graph, since a node can have multiple heads).
    progress: Progress
    deadline: Optional[datetime]  # Can you believe these slackers? The deadline is optional?!
    created_on: datetime  # The moment this item was created; this is generated automatically when this object is made in code.
    modified_on: Optional[datetime]  # The moment this item was update/modified in some way. Generated automatically.
    user: uuid4  # Uniquely identifies the user to whom this work item is assigned. (In real life, this should probably be a list.)


    def __init__(self, title: str, description = "", deadline = None, depends_on = None):
        """
        The constructor method to make one of these WorkItems.

        Args:
            title (str): The name or visible text identifying this task.
            description (str): The textual details of what this task is and what it involves.
            deadline (_type_, optional): A datetime specifying when this task should be completed. If time is irrelevant, use 12 midnight (zero). Defaults to None.
            depends_on (_type_, optional): The list of ids of other tasks that this task must wait for. Defaults to None.
        """

        self.id = uuid4()
        self.title = title
        self.description = description
        self.deadline = deadline
        self.depends_on = depends_on
        self.created_on = now(timezone.utc)
        self.modified_on = self.created_on

# I have left this a little over-engineered, because I was foreseeing adding
# a bunch more method functionality. Some of what could go here is now in
# WorkItemCollection, though that is also a debatable decision. It's somewhat a matter
# of taste until we start to add more actual functionality and features.




