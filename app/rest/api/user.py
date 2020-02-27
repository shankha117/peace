from flask import jsonify, make_response, request, current_app
from . import peace_bp
from werkzeug.exceptions import BadRequest, MethodNotAllowed
from app.rest.utils import expect, required_body, required_params


# from app.rest.services.users import User_Service

@peace_bp.route('/users', methods=['POST'])
@required_body(fields=['type', 'email', 'region'])
def create_user():
    try:
        post_data = request.get_json()

        first_name = expect(post_data.get('first_name'), str, 'first_name')

        first_name = expect(post_data.get('first_name'), str, 'first_name')

        company_name = expect(post_data.get('company_name'), str, 'company_name')

        city = expect(post_data.get('city'), str, 'city')

        state = expect(post_data.get('state'), dict, 'state')

        zip = expect(post_data.get('zip'), dict, 'zip')
        email = expect(post_data.get('email'), dict, 'email')
        web = expect(post_data.get('web'), dict, 'web')
        age = expect(post_data.get('age'), dict, 'age')

        # inserted_id = Cluster_Service().create_cluster(template=template, type=cluster_type,region=region,
        #                                                clustername=clustername, properties=properties)

        return jsonify({'message': 'cluster created', 'cluster_id': first_name}), 200

    except BadRequest as ex:

        return jsonify({'message': str(ex)}), 400

    except Exception as ex:

        return jsonify({'message': str(ex)}), 500

# @peace_bp.route('/users', methods=['GET'])
# @required_params(fields=["page", "limit"])
# def get_all_cluster():
#     try:
#
#         order = expect(request.args.get('order', default='desc'), str, 'order')
#
#         tags = expect(request.args.get('tags'), str, 'tags')
#
#         limit = expect(int(request.args.get('limit')), int, 'limit')
#
#         page = expect(int(request.args.get('page')), int, 'page')
#
#         cluster_type = expect(request.args.get('type'), str, 'type')
#
#         res = Cluster_Service().get_all_clusters(order=order, tags=tags, page=page, limit=limit,
#                                                  cluster_type=cluster_type)
#
#         return jsonify(res), 200
#
#     except BadRequest as ex:
#
#         return jsonify({'message': str(ex)}), 400
#
#     except Exception as ex:
#         import traceback
#
#         return jsonify({'message': str(ex)}), 500
#
#
# @peace_bp.route('/users/<user_id>', methods=['GET'])
# def cluster_details(cluster_id):
#     try:
#         cluster_id = expect(cluster_id, str, 'cluster_id')
#
#         cluster_details = Cluster_Service().get_cluster(cluster_id)
#
#         return jsonify(cluster_details), 200
#
#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500
#
#
# @peace_bp.route('/users/<user_id>', methods=['DELETE'])
# def delete_cluster(cluster_id):
#     try:
#         res = Cluster_Service().delete_cluster(cluster_id=cluster_id)
#
#         if res:
#             return jsonify({'message': 'cluster {0} deleted'.format(cluster_id)}), 200
#
#     except Exception as ex:
#
#         return jsonify({'message': str(ex)}), 500
#
#
# @peace_bp.route('/users/<user_id>', methods=['PUT'])
# @required_body(fields=['key','value'])
# def update_cluster_tags(cluster_id):
#     try:
#         post_data = request.get_json()
#
#         key = expect(post_data.get('key'), str, 'key')
#
#         value = expect(post_data.get('value'), str, 'value')
#
#         return Cluster_Service().update_tags(cluster_id=cluster_id, key=key, value=value)
#
#     except Exception as ex:
#
#         return jsonify({'message': str(ex)}), 500
