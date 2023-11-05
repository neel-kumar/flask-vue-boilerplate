from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

def logicf(btitle):
    return btitle + 'this is from the python server logic :DD'

# sanity check route
@app.route('/ping', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if post_data.get('type') == 'ADD':
            BOOKS.append({
                'title': logicf(post_data.get('title')),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book added!'
        elif post_data.get('type') == 'CLEAR':
            BOOKS.clear()
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
