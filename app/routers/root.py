from typing import Optional

from starlette.responses import FileResponse, RedirectResponse

from fastapi import APIRouter, Depends, Request
from app import templates
from app.utils.auth import AuthCookie, get_auth_cookie

# --------------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------------

router = APIRouter()


# --------------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------------


@router.get(
	path="/",
	summary="Redirect to the login or reminders pages",
	tags=["Pages"],
)
def read_root(
	cookie: Optional[AuthCookie] = Depends(get_auth_cookie),
):
	path = "/reminders" if cookie else "/login"
	return RedirectResponse(url=path, status_code=302)


@router.get(
	path="/favicon.ico",
	include_in_schema=False,
)
async def favicon():
	return FileResponse("static/img/favicon.ico")


@router.get(
	path="/not-found",
	summary='Gets the "Not Found" page',
	tags=["Pages"],
)
async def get_not_found(request: Request):
	return templates.TemplateResponse("pages/not-found.html", {"request": request})
