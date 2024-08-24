# importing Flask and other modules
from flask import Flask, request

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application which URL is associated function
# the complete URL will be http://ip:port/users?name=some_value
@app.route('/users', methods=["GET"])
def say_hello():
    name_value = request.args.get('name')  # "name" is a query parameter

    return "Hello " + name_value


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
