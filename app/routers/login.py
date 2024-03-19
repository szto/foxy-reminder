"""
This module provides routes for authentication.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from app import templates
from app.utils.auth import AuthCookie, get_login_form_creds, get_auth_cookie
from app.utils.exceptions import UnauthorizedPageException

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from pydantic import BaseModel
from typing import Optional


# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter()


# --------------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------------


class UserAccount(BaseModel):
    username: str
    password: str


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------


@router.get("/login", summary="Gets the login page", response_class=HTMLResponse)
async def get_login(
    request: Request,
    invalid: Optional[bool] = None,
    logged_out: Optional[bool] = None,
    unauthorized: Optional[bool] = None,
):
    context = {
        "request": request,
        "invalid": invalid,
        "logged_out": logged_out,
        "unauthorized": unauthorized,
    }
    return templates.TemplateResponse("pages/login.html", context)


@router.post("/login", summary="Logs into the app")
async def post_login(
    cookie: Optional[AuthCookie] = Depends(get_login_form_creds),
) -> dict:
    if cookie:
        response = RedirectResponse("/reminders", status_code=302)
        response.set_cookie(key=cookie.name, value=cookie.token)
    else:
        response = RedirectResponse("/login?invalid=True", status_code=302)
    return response


@router.post("/logout", summary="Logs out of the app")
async def post_logout(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> dict:
    if not cookie:
        raise UnauthorizedPageException()

    response = Response(status_code=302)
    response.set_cookie(key=cookie.name, value=cookie.token, expires=-1)
    response.headers["HX-Redirect"] = "/login?logged_out=True"
    return response
