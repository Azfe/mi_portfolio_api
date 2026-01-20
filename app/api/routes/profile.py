from fastapi import APIRouter

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@router.get("/")
def get_profile():
    return {"detail": "Not implemented"}