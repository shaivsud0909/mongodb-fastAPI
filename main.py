from fastapi import FastAPI
from schema import UserSchema
from database import users

app=FastAPI()

@app.get("/read",response_model=list[UserSchema])
async def read_fun():
    users_list=[]
    cursor= users.find()
    async for user in cursor:
        users_list.append(user)
    return users_list


@app.put("/add")
async def create_fun(user:  UserSchema):
    res=await users.insert_one(user.model_dump())
    return{        
    "message": "User created",
        "id": str(res.inserted_id)
    }

    
@app.delete("/delete/{name}")
async def delete_user(name: str):
    result = await users.delete_many({"name": name})
    return{        
    "message": "User deleted",
        "deleted": result.deleted_count
    }
    

@app.put("/update/{old_name}")
async def update_fun(name: str, new_name: str, is_active: bool):
    result = await users.update_many(
        {"name": name},
        {"$set": {"name": new_name, "is_active": is_active}}
    )
    return {
        "message": "User updated",
        "matched": result.matched_count
    }

