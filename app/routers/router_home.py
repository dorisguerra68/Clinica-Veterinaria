from fastapi import APIRouter

router=APIRouter()

@router.get("/, tags="Home")
def home():
    return {"mensage":"Ecomerce API FenCoders Madrid P5"}