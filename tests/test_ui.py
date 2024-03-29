# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import re

from playwright.sync_api import Page, expect
from testlib.inputs import User


# --------------------------------------------------------------------------------
# Login Behaviors
#
#   log in successfully
#   no login credentials
#   no username
#   no password
#   incorrect username
#   incorrect password
#   log out
# --------------------------------------------------------------------------------


def test_successful_login(page: Page, user: User):
    # Given the login page is displayed
    page.goto("/login")

    # When the user logs into the app with valid credentials
    page.locator('[name="username"]').fill(user.username)
    page.locator('[name="password"]').fill(user.password)
    page.click("#login")

    # Then the reminders page is displayed
    expect(page).to_have_title("Reminders | Foxy Reminders app")
    expect(page).to_have_url(re.compile(re.escape("/") + "reminders"))
    expect(page.locator("id=foxy-logo")).to_be_visible()
    expect(page.locator("id=foxy-title")).to_have_text("Foxy Reminders")
    expect(page.locator("id=reminders-message")).to_have_text(f"Reminders for {user.username}")
    expect(page.get_by_role("button", name="Logout")).to_be_visible()


def test_failed_login(page: Page, user: User):
    # Given the login page is displayed
    page.goto("/login")

    # When the user logs into the app with invalid credentials
    page.locator('[name="username"]').fill("wrong_username")
    page.locator('[name="password"]').fill("wrong_password")
    page.click("#login")

    # Then the redirect login page with is invalid
    expect(page).to_have_url("http://127.0.0.1:8000/login?invalid=True")
    expect(page).to_have_url(re.compile("/login"))


# --------------------------------------------------------------------------------
# Navigation Behaviors
#
#   load the login page
#   load the reminders page
#   home redirects to login when not authenticated
#   home redirects to reminders when logged in
#   invalid navigation redirects to not found
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# Reminders Behaviors
#
#   the initial reminders page is empty
#   create the first list
#   create more lists
#   create the first item in a list
#   create more items in a list
#   strike an item as completed
#   unstrike an item from being completed
#   edit the name of an uncompleted item
#   edit the name of a completed item
#   begin editing the name of a list but cancel by clicking X
#   begin editing the name of a list but cancel by clicking away
#   delete an item
#   delete all items
#   creat new items after deleting all items in a list
#   select a different list
#   edit the name of an unselected list
#   edit the name of a selected list
#   commit an edit by clicking check
#   commit an edit by typing ENTER
#   begin editing the name of a list but cancel by clicking X
#   begin editing the name of a list but cancel by clicking away
#   delete an unselected list
#   delete a selected list
#   delete all lists
#   create new lists after deleting all lists
#   verify only one row (list or item) may be edited at a time:
#     list name
#     new list name
#     item description
#     new item description
#   data persists after page refresh
#   data persists after logout and log back in
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# User Behaviors
#
#   log in as separate users in separate sessions
#   one user cannot see another user's reminders
# --------------------------------------------------------------------------------
