from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def history_test():
    return {
        "status": "ok",
        "message": "History router is working"
    }


@router.get("/")
def get_history():
    return {
        "status": "ok",
        "history": []
    }