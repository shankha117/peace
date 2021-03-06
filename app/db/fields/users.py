"""
Users
"""
from enum import Enum


class User(Enum):
    """
    Status for the projects, documents and job
    """
    ID = 'id'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    COMPANY_NAME = 'company_name'
    CITY = 'city'
    STATE = 'state'
    ZIP = 'zip'
    EMAIL = 'email'
    WEB = 'web'
    AGE = 'age'