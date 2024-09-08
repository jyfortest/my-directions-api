from flask import Blueprint, request, jsonify
from controllers.directions_controller import get_shortest_route

directions_bp = Blueprint('directions', __name__)

@directions_bp.route('/directions', methods=['POST'])
def directions():
    data = request.get_json()

    start = data.get('start')
    goal = data.get('goal')

    if not start or not goal:
        return jsonify({"error": "start and goal are required"}), 400
    
    result = get_shortest_route(start, goal)

    return jsonify(result)
