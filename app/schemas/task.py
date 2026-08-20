from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"
    assignee_id: int | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    assignee_id: int | None = None


class TaskResponse(TaskBase):
    id: int
    project_id: int
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)