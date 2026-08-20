from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(docs_url="/")

@app.get("/test")
def get_test():
    return {
        "status": "Khơi động thành công",
        "algorithm": settings.ALGORITHM,
        "token_expire": settings.ACCESS_TOKEN_EXPIRE_MINUTES
    }