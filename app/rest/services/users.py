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
                                                            page=page - 1, limit=limit)

            next = True if count > (limit * page) else False

            res = {"data": data, "count": count, "more": next}

            return res

        except Exception as e:
            import traceback
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)

    def delete_user(self, user_id: int):

        try:
            if not User_Data_Layer().get_user_details(user_id):
                return jsonify({'error': 'no user with the id {0} exists'.format(user_id)}), 400

            # delete the user

            return User_Data_Layer().delete_user(user_id=user_id)

        except Exception as e:
            import traceback
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)

    def update_user(self, user_id: int, first_name: str, last_name: str, age: int):

        try:
            if not User_Data_Layer().get_user_details(user_id):
                return jsonify({'error': 'no user with the id {0} exists'.format(user_id)}), 400

            result = User_Data_Layer().update_user(user_id=user_id, first_name=first_name, last_name=last_name, age=age)

            if result != 0:
                current_app.logger.info('{0} user updated'.format(result))
                return jsonify({'message': '{0} user updated'.format(result)}), 200

            return jsonify({'message': 'no user updated'.format(result)}), 200

        except Exception as e:
            import traceback
            current_app.logger.error(traceback.format_exc())
            raise Exception(e)
