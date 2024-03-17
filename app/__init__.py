"""
This module builds shared parts for other modules.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import json
import tinydb
from fastapi.templating import Jinja2Templates
from app.utils.persistence import RemindersTable


# --------------------------------------------------------------------------------
# Read Configuration
# --------------------------------------------------------------------------------

with open('config.json') as config_json:
  config = json.load(config_json)
  users = config['users']


# --------------------------------------------------------------------------------
# Establish the Secret Key
# --------------------------------------------------------------------------------

secret_key = config['secret_key']


# --------------------------------------------------------------------------------
# Connect the Database
# --------------------------------------------------------------------------------

reminders_table = RemindersTable()



# --------------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------------

templates = Jinja2Templates(directory="templates")