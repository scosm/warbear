
from fastapi import FastAPI, HTTPException
from app.backend.model.WorkItem import WorkItem
from app.backend.model.WorkItemCollection import WorkItemCollection

app = FastAPI(title="Warbear: Your Work Item Board!")

