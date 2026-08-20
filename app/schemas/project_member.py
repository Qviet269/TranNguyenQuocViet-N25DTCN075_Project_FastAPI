from pydantic import BaseModel, ConfigDict


class ProjectMemberBase(BaseModel):
    user_id: int
    role: str = "member"


class ProjectMemberCreate(ProjectMemberBase):
    pass


class ProjectMemberUpdate(BaseModel):
    role: str | None = None


class ProjectMemberResponse(ProjectMemberBase):
    id: int
    project_id: int

    model_config = ConfigDict(from_attributes=True)