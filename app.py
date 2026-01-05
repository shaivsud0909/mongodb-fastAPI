from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import asyncio

#schema
class schema(BaseModel):
    name:str
    is_active:bool

async def fun():
    #connect
    client=AsyncIOMotorClient("mongodb://localhost:27017")
    db=client.test_db
    users=db.users

    #create
    user1 = schema(name="Shaiv",is_active=True)
    user2 = schema(name="Gyanendra",is_active=False)
    result = await users.insert_many([ user1.model_dump(), user2.model_dump()]) #Pydantic object  -> .model_dump()  ->  MongoDB


    #read
    active_users = users.find({"is_active": True})
    async for user in active_users:
        print(user)

    #update
    await users.update_many({"is_active":True},{"$set":{"is_active":False}})

    #delete
    await users.delete_many({"name": "Shaiv"})

asyncio.run(fun())    





