from myapi.default_config import SQLALCHEMY_DATABASE_URI


import os
DEBUG=True

SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")