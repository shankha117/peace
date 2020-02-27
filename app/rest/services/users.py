from app.db.services.user import User_Data_Layer
from flask import current_app, jsonify


class User_Service(object):

    def create_user(self, id: int, first_name: str, last_name: str, company_name: str,
                    city: str, state: str, zip: int,
                    email: str, web: str, age: int):
        try:

            return User_Data_Layer().create_user(id=id, first_name=first_name, last_name=last_name,
                                                 company_name=company_name, city=city,
                                                 state=state, zip=zip
                                                 , email=email, web=web, age=age)

        except Exception as e:
            raise Exception(str(e))

    def get_user(self, user_id: int):

        try:

            data = User_Data_Layer().get_user_details(user_id)
            if data:
                return data
            return {"message": "no users found"}

        except Exception as e:
            raise Exception(e)

    def get_all_users(self, sort: str, name: str, page: int, limit: int):

        try:
            sort_order = None
            attribute = None
            if sort:
                sort_order = 'asc'
                if sort[0] == '-':
                    sort_order = 'dsc'
                    attribute = sort[1:]
                else:
                    attribute = sort

            print(sort_order, attribute, name, page, limit)

            data, count = User_Data_Layer().get_all_cluster(sort_order=sort_order, sort_by=attribute, name=name,
                                                            page=page-1, limit=limit)

            next = True if count > (limit * page) else False

            res = {"data": data, "count": count, "more": next}

            return res

        except Exception as e:
            import traceback
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)
    #
    # def delete_cluster(self, cluster_id: str):
    #
    #     try:
    #         if not Cluster_Data_Layer().get_cluster_details(cluster_id):
    #             return jsonify({'error': 'no cluster with the id {0} exists'.format(cluster_id)}), 400
    #
    #         # delete all child clusters
    #         Instance_Data_Layer().delete_all_instance_by_cluster_id(cluster_id=cluster_id)
    #
    #         # delete the cluster document
    #         return Cluster_Data_Layer().delete_cluster(cluster_id=cluster_id)
    #
    #     except Exception as e:
    #         import traceback
    #         current_app.logger.error(traceback.format_exc())
    #         raise Exception(e)
    #
    # def add_tags(self, cluster_id: str, tags: list):
    #
    #     try:
    #         if not Cluster_Data_Layer().get_cluster_details(cluster_id):
    #             return jsonify({'error': 'no cluster with the id {0} exists'.format(cluster_id)}), 400
    #
    #         result = Cluster_Data_Layer().add_tags(cluster_id=cluster_id, tags=tags)
    #
    #         if result != 0:
    #             return jsonify({'message': '{0} cluster updated'.format(result)}), 200
    #
    #         return jsonify({'error': 'Some tags might already be present. {0} cluster '
    #                                  'updated'.format(result)}), 200
    #
    #     except Exception as e:
    #         import traceback
    #         current_app.logger.error(traceback.format_exc())
    #         raise Exception(e)
    #
    # def update_tags(self, cluster_id: str, key: str, value: str):
    #
    #     try:
    #         if not Cluster_Data_Layer().get_cluster_details(cluster_id):
    #             return jsonify({'error': 'no cluster with the id {0} exists'.format(cluster_id)}), 400
    #
    #         result = Cluster_Data_Layer().update_tag(cluster_id=cluster_id, key=key, value=value)
    #
    #         if result != 0:
    #             return jsonify({'message': '{0} cluster updated'.format(result)}), 200
    #
    #         return jsonify({'error': 'key to be updated not present Or has the same value provide.  {0} cluster '
    #                                  'updated .'.format(result)}), 200
    #
    #     except Exception as e:
    #         import traceback
    #         current_app.logger.error(traceback.format_exc())
    #         raise Exception(e)
    #
    # def delete_tags(self, cluster_id: str, keys: list):
    #
    #     try:
    #         if not Cluster_Data_Layer().get_cluster_details(cluster_id):
    #             return jsonify({'error': 'no cluster with the id {0} exists'.format(cluster_id)}), 400
    #
    #         result = Cluster_Data_Layer().delete_tag(cluster_id=cluster_id, key_list=keys)
    #
    #         if result != 0:
    #             return jsonify({'message': '{0} cluster updated'.format(result)}), 200
    #
    #         return jsonify({'error': 'key or keys to be deleted not present.  {0} cluster '
    #                                  'updated .'.format(result)}), 200
    #
    #     except Exception as e:
    #         import traceback
    #         current_app.logger.error(traceback.format_exc())
    #         raise Exception(e)
