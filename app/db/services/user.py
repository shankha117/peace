from app.db.mongo_db_model import Model
from flask import current_app
from datetime import datetime
from bson.objectid import ObjectId
import re
from app.db.fields.users import User
import traceback


class User_Data_Layer(Model):

    def __init__(self):

        self._collection = 'peace_users'

    def create_user(self, id: int, first_name: str, last_name: str, company_name: str,
                    city: str, state: str, zip: int,
                    email: str, web: str, age: int):

        try:
            doc = {
                User.ID.value: id,
                User.FIRST_NAME.value: first_name,
                User.LAST_NAME.value: last_name,
                User.COMPANY_NAME.value: company_name,
                User.CITY.value: city,
                User.STATE.value: state,
                User.ZIP.value: zip,
                User.EMAIL.value: email,
                User.WEB.value: web,
                User.AGE.value: age
            }

            data = self.save(doc, index=User.ID.value)

            user_id = data.inserted_id

            current_app.logger.info("new user created {0}".format(user_id))

            return user_id

        except Exception as e:
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)

    def get_user_details(self, user_id):

        try:

            data = self.search_one(user_id)
            return data

        except Exception as e:
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)

    def get_all_users(self, sort_order: str, sort_by: str, name: str, page: int, limit: int):

        try:
            match = {}

            if name:
                # make the regex for substring matching with case sensitive
                regx = re.compile("^" + name, re.IGNORECASE)

                # make the match query
                match["$or"] = [{User.FIRST_NAME.value: {"$regex": regx}},
                                {User.LAST_NAME.value: {"$regex": regx}}]

            data, count = self.search_bulk(match=match, sort_order=sort_order, sort_by=sort_by, page=page, limit=limit,
                                           project={})

            return data, count

        except Exception as e:
            current_app.logger.error(e)
            raise Exception(e)

    def delete_user(self, user_id: int):

        try:
            query = {"id": user_id}

            return self.delete_one(query)

        except Exception as e:
            current_app.logger.error(e)
            raise Exception(e)

    def update_user(self, user_id: int, first_name: str, last_name: str, age: int):

        try:
            query_doc = {}

            if first_name:
                query_doc[User.FIRST_NAME.value] = first_name
            if last_name:
                query_doc[User.LAST_NAME.value] = last_name
            if age:
                query_doc[User.AGE.value] = age

            set_query = {"$set": query_doc}

            return self.update_one(id=user_id, set_query=set_query)

        except Exception as e:
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)
