from fastapi.routing import APIRouter


router = APIRouter(
    prefix = "/users",
    tags = ["users"],
    dependencies=[]

    )

@router.get("/")
def get_users():
    return {"message":"A user from Inventory system"}

@router.post("/")
def new_user():
    return {"message":"A new user"}

@router.get("/{id}")
def get_user(id:int):
    return {"message":"A user by id from Inventory system"}

@router.patch("/{id}")
def update_user(id:int):
    return {"message":"A user by ID updated"}

@router.delete("/{id}")
def delete_user(id:int):
    return {"message":"A user by ID deleted"}

