from flask import Flask, jsonify;
app = Flask(__name__);


# We are also adding some response headers in the after_request function 
# that will allow cross-origin resource sharing (CORS).

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greeting', methods=['GET'])
def get_tasks():
    return '{"id":36,"content":"Hello, World!"}';

if __name__ == '__main__':
    app.run(debug=True);