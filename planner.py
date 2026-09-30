from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def planners_test():
    return {
        "status": "ok",
        "message": "Planners router is working"
    }


@router.post("/home")
def home_planner():
    return {
        "status": "ok",
        "planner": "Home Planner",
        "message": "Home planner is working"
    }


@router.post("/party")
def party_planner():
    return {
        "status": "ok",
        "planner": "Party Planner",
        "message": "Party planner is working"
    }


@router.post("/jewelry")
def jewelry_planner():
    return {
        "status": "ok",
        "planner": "Jewelry Planner",
        "message": "Jewelry planner is working"
    }