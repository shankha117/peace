"""
This module contains all database interfacing methods for the MFlix
application. You will be working on this file for the majority of M220P.

Each method has a short description, and the methods you must implement have
docstrings with a short explanation of the task.

Look out for TODO markers for additional help. Good luck!
"""

from flask import current_app, g
from werkzeug.local import LocalProxy
import json
from pymongo import MongoClient, DESCENDING, ASCENDING


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    PEACE_DB_HOST = current_app.config["mongo_db_host"]
    PEACE_DB_PORT = current_app.config["mongo_db_port"]
    PEACE_DB_NAME = current_app.config["mongo_db_name"]
    PEACE_DB_AUTH = current_app.config['mongo_db_auth']
    PEACE_DB_USER = current_app.config['mongo_db_user']
    PEACE_DB_PASSWORD = current_app.config['mongo_db_password']

    if db is None:
        db = g._database = MongoClient(
            PEACE_DB_HOST,
            int(PEACE_DB_PORT),
            maxPoolSize=50,
            wtimeout=2500,
            # connectTimeoutMS=200,
        )
        # user authentication for mongodb
        auth = json.loads(PEACE_DB_AUTH.lower())
        if auth:
            db.the_database.authenticate(PEACE_DB_USER, PEACE_DB_PASSWORD, source=PEACE_DB_NAME)

    return db[PEACE_DB_NAME]


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)
