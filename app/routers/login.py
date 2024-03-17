"""
This module provides routes for authentication.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from ..auth import AuthCookie, get_login_form_creds, get_auth_cookie

from fastapi import APIRouter, Cookie, Depends, Response
from pydantic import BaseModel


# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter(prefix="/auth")


# --------------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------------

class UserAccount(BaseModel):
    username: str
    password: str


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------

@router.post("/login", summary="Logs into the app")
async def post_login(response: Response, cookie: AuthCookie = Depends(get_login_form_creds)) -> dict:
    response.set_cookie(key=cookie.name, value=cookie.token)
    return {"message": f"Logged in as {cookie.username}"}


@router.post("/logout", summary="Logs out of the app")
async def post_login(response: Response, cookie: AuthCookie = Depends(get_auth_cookie)) -> dict:
    response.set_cookie(key=cookie.name, value=cookie.token, expires=-1)
    return {"message": f"Logged out as {cookie.username}"}