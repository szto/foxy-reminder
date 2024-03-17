"""
This module provides routes for the API.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from app.utils.auth import get_username_for_api
from app.utils.exceptions import NotFoundException, ForbiddenException

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from tinydb import Query


# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter(prefix="/api")


# --------------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------------

class ReminderItem(BaseModel):
    description: str
    completed: bool


class ReminderList(BaseModel):
    id: int
    owner: str
    name: str
    reminders: list[ReminderItem] | None

class NewReminderList(BaseModel):
    name: str


class UpdatedReminderList(BaseModel):
    name: str
    reminders: list[ReminderItem]


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@router.get("/reminders", summary="Get the user's reminder lists", response_model=list[ReminderList])
async def get_reminders(
    username: str = Depends(get_username_for_api)
    ) -> list[ReminderList]:
    """
    Gets the list of all reminder lists owned by the user.
    """
    return storage.get_lists(username)


@router.post("/reminders", summary="Create a new reminder list", response_model=ReminderList)
async def post_reminders(
    reminder_list: NewReminderList,
    username: str = Depends(get_username_for_api)
) -> ReminderList:
    list_id = storage.create_list(
        reminder_list.name,
        username,
        reminder_list.reminders
    )
    return storage._get_raw_list(list_id, username)


@router.get("/reminders/{list_id}", summary="Get a reminder list by ID", response_model=ReminderList)
async def get_list_id(
    list_id: int,
    username: str = Depends(get_username_for_api)
) -> ReminderList:
    return storage._get_raw_list(list_id, username)


@router.put("/reminders/{list_id}", summary="Fully updates a reminder list", response_model=ReminderList)
async def put_list_id(
    list_id: int,
    reminder_list: UpdatedReminderList,
    username: str = Depends(get_username_for_api)
) -> ReminderList:
    data = reminder_list.dict()
    storage.update_list(list_id, data, username)
    return storage._get_raw_list(list_id, username)


@router.delete("/reminders/{list_id}", summary="Deletes a reminder list", response_model=dict)
async def delete_list_id(
    list_id: int,
    username: str = Depends(get_username_for_api)
) -> dict:
    storage.delete_list(list_id, username)
    return dict()