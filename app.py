from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/posts', methods=['POST'])
def create_post():
    # Get data from the request
    data = request.json
    print(data)
    # Add the new post to the list of posts
    new_post = {
        'userId': data['userId'],
        'id': 1,
        'title': data['title'],
        'body': data['body']
    }
    
    # Return the new post as JSON
    return jsonify(new_post), 201
if __name__ == '__main__':
    app.run(debug=True)