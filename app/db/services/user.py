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

            cluster_id = data.inserted_id

            current_app.logger.info("new user created {0}".format(cluster_id))

            return cluster_id

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

    def get_all_cluster(self, sort_order: str, sort_by: str, name: str, page: int, limit: int):

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

    # def delete_cluster(self, cluster_id: str):
    #
    #     try:
    #         query = {"_id": ObjectId(cluster_id)}
    #
    #         return self.delete_one(query)
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
    #
    # def add_tags(self, cluster_id: str, tags: list):
    #
    #     try:
    #         tags_list = list(i[Cluster.tags_key.value['rel']] for i in tags)
    #
    #         query_string = {Cluster.tags_key.value['abs']: {"$nin": tags_list}}
    #
    #         set_query = {"$addToSet": {Cluster.tags.value['abs']: {"$each": tags}}}
    #
    #         return self.update_one(id=cluster_id, match_query=query_string, set_query=set_query)
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
    #
    # def update_tag(self, cluster_id: str, key: str, value: str):
    #
    #     try:
    #         query_string = {Cluster.tags.value['abs']: {"$elemMatch": {Cluster.tags_key.value['rel']: key}}}
    #
    #         set_query = {"$set": {Cluster.tags.value['abs'] + ".$." + Cluster.tags_value.value['rel']: value}}
    #
    #         return self.update_one(id=cluster_id, match_query=query_string, set_query=set_query)
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
    #
    # def delete_tag(self, cluster_id: str, key_list: list):
    #
    #     try:
    #         query_string = {}
    #
    #         set_query = {"$pull": {Cluster.tags.value['abs']: {Cluster.tags_key.value['rel']:
    #                                                                {"$in": key_list}}}}
    #
    #         return self.update_one(id=cluster_id, match_query=query_string, set_query=set_query)
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
