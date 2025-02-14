from fastapi import FastAPI
from app.routes import router  # ✅ 應該匯入 `router`，而不是 `routes`

app = FastAPI()

app.include_router(router)  # ✅ 確保 `router` 被加入 FastAPI 應用

@app.get("/")
def root():
    return {"message": "Stock Monitor API is running"}
