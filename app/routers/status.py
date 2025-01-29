from http import HTTPStatus
from fastapi import APIRouter
from app.database.engine import check_availability
from app.models.AppStatus import AppStatus

router = APIRouter()


# app status servers
@router.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    check_availability()
    return AppStatus(database=check_availability())
