from fastapi import APIRouter

router = APIRouter()  # ✅ 確保這一行存在

@router.get("/stocks")
def get_stocks():
    return {"message": "Stock API is working"}
