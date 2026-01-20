from fastapi import APIRouter

router = APIRouter(
    prefix="/cv",
    tags=["cv"],
)


@router.get("/")
def get_cv():
    return {"detail": "Not implemented"}