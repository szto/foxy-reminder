"""
This module provides routes for the API.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from app import storage
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
    reminders_id = storage.create_list(
        reminder_list.name,
        username,
        reminder_list.reminders
    )
    return storage.get_list(reminders_id, username)


@router.get("/reminders/{reminders_id}", summary="Get a reminder list by ID", response_model=ReminderList)
async def get_reminders_id(
    reminders_id: int,
    username: str = Depends(get_username_for_api)
) -> ReminderList:
    return storage.get_list(reminders_id, username)


@router.put("/reminders/{reminders_id}", summary="Fully updates a reminder list", response_model=ReminderList)
async def put_reminders_id(
    reminders_id: int,
    reminder_list: UpdatedReminderList,
    username: str = Depends(get_username_for_api)
) -> ReminderList:
    data = reminder_list.dict()
    storage.update_list(reminders_id, data, username)
    return storage.get_list(reminders_id, username)


@router.delete("/reminders/{reminders_id}", summary="Deletes a reminder list", response_model=dict)
async def delete_reminders_id(
    reminders_id: int,
    username: str = Depends(get_username_for_api)
) -> dict:
    storage.delete_list(reminders_id, username)
    return dict()