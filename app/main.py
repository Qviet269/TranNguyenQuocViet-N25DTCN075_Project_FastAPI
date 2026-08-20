from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exception_handlers import http_exception_handler
from app.db.database import Base, engine, get_db

from app.models.user import User
from app.models.project import Project
from app.models.project_member import ProjectMember
from app.models.task import Task


Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")


app.add_exception_handler(HTTPException, http_exception_handler)

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {
        "success": True,
        "message": "Database session hoạt động"
    }

@app.get("/health")
def get_health():
    return {
        "status": "Khởi động thành công",
        "algorithm": settings.ALGORITHM,
        "token_expire": settings.ACCESS_TOKEN_EXPIRE_MINUTES
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="student_id phải lớn hơn 0"
        )

    if student_id == 999:
        raise HTTPException(
            status_code=404,
            detail="Không tìm thấy student"
        )

    return {
        "success": True,
        "student_id": student_id
    }

@app.get("/admin")
def admin_api(role: str):

    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Bạn không có quyền truy cập"
        )

    return {
        "success": True,
        "message": "Truy cập thành công"
    }