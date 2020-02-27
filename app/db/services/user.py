from app.db.mongo_db_model import Model
from flask import current_app
from datetime import datetime
from bson.objectid import ObjectId
from app.db.fields.users import User


class User_Data_Layer(Model):

    def __init__(self):

        self._collection = 'cluster'

    def create_cluster(self, template: str, type: str, region: str, clustername: str, properties: dict):

        try:
            doc = {
                User.template.value: template,
                User.type.value: type,
                User.region.value: region,
                User.cluster_name.value: clustername,
                User.properties.value: properties,
                User.created_date.value: datetime.now(),
                User.updated_date.value: datetime.now()
            }

            data = self.save(doc, index=User.cluster_name.value)

            cluster_id = data.inserted_id

            current_app.logger.info("cluster created {0}".format(cluster_id))

            return cluster_id

        except Exception as e:
            current_app.logger.error(e)
            raise Exception(e)
    #
    # def get_cluster_details(self, cluster_id):
    #
    #     try:
    #
    #         data = self.search_one(cluster_id)
    #         return data
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
    #
    # def get_all_cluster(self, order: str, tags: str, type: str, page: int, limit: int):
    #
    #     try:
    #         match = {}
    #
    #         if tags:
    #             all_array = []
    #             for i in eval(tags):
    #                 all_array.append({"$elemMatch": i})
    #
    #             match[Cluster.tags.value['abs']] = {"$all": all_array}
    #
    #         if type:
    #             match[Cluster.type.value] = type
    #
    #         data, count = self.search_bulk(match=match, order=order, page=page, limit=limit, project={})
    #
    #         return data, count
    #
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception(e)
    #
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
