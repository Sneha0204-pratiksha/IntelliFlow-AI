from pydantic import BaseModel


class WorkflowCreate(BaseModel):
    title: str
    description: str
    created_by: str


class WorkflowUpdate(BaseModel):
    title: str
    description: str
    status: str