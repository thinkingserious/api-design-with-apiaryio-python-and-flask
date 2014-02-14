#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

folders = [
    {
        "id": 1,
        "name": "Health",
        "description": "This represents projects that are related to health",
        "parent": 0,
        "meta": "NULL"
    },
    {
        "id": 2,
        "name": "Diet",
        "description": "A collection of projects related to Diet",
        "parent": 1,
        "meta": "NULL"
    }
]

@app.route('/folder/<int:folder_id>', methods = ['GET'])
def get_folder(folder_id):
    folder = filter(lambda t: t['id'] == folder_id, folders)
    if len(folder) == 0:
        abort(404)
    return jsonify( folder[0] )

@app.route('/folder', methods = ['GET'])
def get_folders():
    return jsonify( { 'folders': folders } )

@app.route('/folder', methods = ['POST'])
def create_folder():
    if (not request.json) or (not 'name' in request.json) or (not 'description' in request.json):
        abort(400)
    folder = {
        'id': folders[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json['description'],
        'parent': request.json['parent'],
        'meta': request.json.get('meta', "NULL")
    }
    folders.append(folder)
    return jsonify( folder ), 201

@app.route('/folder/<int:folder_id>', methods = ['PATCH'])
def update_folder(folder_id):
    folder = filter(lambda t: t['id'] == folder_id, folders)
    if len(folder) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'parent' in request.json and type(request.json['parent']) is not int:
        abort(400)
    if 'meta' in request.json and type(request.json['meta']) is not str:
        abort(400)
    folder[0]['name'] = request.json.get('name', folder[0]['name'])
    folder[0]['description'] = request.json.get('description', folder[0]['description'])
    folder[0]['parent'] = request.json.get('parent', folder[0]['parent'])
    folder[0]['meta'] = request.json.get('meta', folder[0]['meta'])
    return jsonify( folder[0] )

@app.route('/folder/<int:folder_id>', methods = ['DELETE'])
def delete_folder(folder_id):
    folder = filter(lambda t: t['id'] == folder_id, folders)
    if len(folder) == 0:
        abort(404)
    folders.remove(folder[0])
    return jsonify( { "result": True } )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { "error": "Resource not found" } ), 404)

@app.errorhandler(400)
def create_failed(error):
    return make_response(jsonify( { "error": "Resource modification failed" } ), 400)

if __name__ == '__main__':
    app.run(debug = True)
