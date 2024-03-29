"""
This module builds shared parts for other modules.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import json
from fasthx import Jinja
from fastapi.templating import Jinja2Templates


# --------------------------------------------------------------------------------
# Read Configuration
# --------------------------------------------------------------------------------

with open("config.json") as config_json:
    config = json.load(config_json)
    users = config["users"]
    db_path = config["db_path"]


# --------------------------------------------------------------------------------
# Establish the Secret Key
# --------------------------------------------------------------------------------

secret_key = config["secret_key"]


# --------------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------------

templates = Jinja2Templates(directory="templates")
jinja = Jinja(templates)
