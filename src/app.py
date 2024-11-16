from bson import ObjectId
import logging
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.auth_db
users_collection = db.users

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/users', methods=['GET'])
def get_users():
    logging.debug(f"Request headers: {request.headers}")
    logged_in_user = request.headers.get('X-Logged-In-UserName')
    if not logged_in_user:
        logging.error("X-Logged-In-User header is missing")
        return jsonify({"error": "X-Logged-In-User header is missing"}), 400

    logged_in_user_name = logged_in_user # ObjectId(logged_in_user)

    logging.debug(f"Logged in user: {logged_in_user_name}")
    users = list(users_collection.find({"username": {"$ne": logged_in_user_name}}, {"_id": 0}))
    logging.debug(f"Users found: {users}")

    if not users:
        logging.warning("No users found")
        return jsonify({"message": "No users found"}), 404

    return jsonify(users), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    mobile = data.get('mobile')
    name = data.get("name")
    sent_requests = []
    received_requests = []
    friends = []
    
    if users_collection.find_one({"username": username}):
        return jsonify({"message": "User already exists"}), 400
    
    users_collection.insert_one({
        "username": username,
        "password": password,
        "email": email,
        "mobile": mobile,
        "name": name,
        "sent_requests": sent_requests,
        "received_requests": received_requests,
        "friends": friends
    })
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        return jsonify({"message": "Login successful", "userId": str(user['_id']), "username": str(user['username'])}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/delete-all-users', methods=['DELETE'])
def delete_all_users():
    result = users_collection.delete_many({})
    return jsonify({"message": f"Deleted {result.deleted_count} users"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)