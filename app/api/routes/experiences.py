from fastapi import APIRouter

router = APIRouter(
    prefix="/experiences",
    tags=["experiences"],
)


@router.get("/")
def get_experiences():
    return {"detail": "Not implemented"}