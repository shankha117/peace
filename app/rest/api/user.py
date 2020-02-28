from flask import jsonify, make_response, request, current_app
from . import peace_bp
from werkzeug.exceptions import BadRequest, MethodNotAllowed
from app.rest.utils import expect, required_body, required_params
from app.rest.services.users import User_Service


@peace_bp.route('/users', methods=['POST'])
@required_body(fields=['id', 'first_name', 'email'])
def create_user():
    try:
        post_data = request.get_json()

        id = expect(post_data.get('id'), int, 'id')

        first_name = expect(post_data.get('first_name'), str, 'first_name')

        last_name = expect(post_data.get('last_name'), str, 'last_name')

        company_name = expect(post_data.get('company_name'), str, 'company_name')

        city = expect(post_data.get('city'), str, 'city')

        state = expect(post_data.get('state'), str, 'state')

        zip = expect(post_data.get('zip'), int, 'zip')

        email = expect(post_data.get('email'), str, 'email')

        web = expect(post_data.get('web'), str, 'web')

        age = expect(post_data.get('age'), int, 'age')

        inserted_id = User_Service().create_user(id=id, first_name=first_name, last_name=last_name,
                                                 company_name=company_name, city=city,
                                                 state=state, zip=zip, email=email, web=web,
                                                 age=age)

        return jsonify({'message': 'new user created', 'user_id': inserted_id}), 201

    except BadRequest as ex:

        return jsonify({'message': str(ex)}), 400

    except Exception as ex:

        return jsonify({'message': str(ex)}), 500


@peace_bp.route('/users', methods=['GET'])
@required_params(fields=["page"])
def get_all_cluster():
    try:

        name = expect(request.args.get('name'), str, 'name')

        sort = expect(request.args.get('sort'), str, 'sort')

        limit = expect(int(request.args.get('limit', default=5)), int, 'limit')

        page = expect(int(request.args.get('page')), int, 'page')

        res = User_Service().get_all_users(sort=sort, name=name, page=page, limit=limit)

        return jsonify(res), 200

    except BadRequest as ex:

        return jsonify({'message': str(ex)}), 400

    except Exception as ex:
        import traceback

        return jsonify({'message': str(ex)}), 500


@peace_bp.route('/users/<user_id>', methods=['GET'])
def user_details(user_id):
    try:
        user_id = expect(user_id, str, 'user_id')

        user_details = User_Service().get_user(user_id=int(user_id))

        return jsonify(user_details), 200

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@peace_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        res = User_Service().delete_user(user_id=int(user_id))
        if res:
            current_app.logger.info('user {0} deleted'.format(user_id))
            return jsonify({'message': 'user {0} deleted'.format(user_id)}), 200

    except Exception as ex:

        return jsonify({'message': str(ex)}), 500


@peace_bp.route('/users/<user_id>', methods=['PUT'])
@required_body(fields=[])
def update_user(user_id):
    try:
        post_data = request.get_json()

        first_name = expect(post_data.get('first_name'), str, 'first_name')

        last_name = expect(post_data.get('last_name'), str, 'last_name')

        age = expect(post_data.get('age'), int, 'age')

        return User_Service().update_user(user_id=int(user_id), first_name=first_name, last_name=last_name, age=age)

    except Exception as ex:

        return jsonify({'message': str(ex)}), 500
