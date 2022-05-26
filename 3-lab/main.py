from flask import Flask

import random

### Make the flask app
app = Flask(__name__)

### Routes
@app.route('/')
def index():

    array = ["Vlad", "Didovets", "KID-21"]

    random_thing = random.randrange(len(array))

    if (array[random_thing]) == "Vlad":
        return "Vlad Hello, world!"
    elif (array[random_thing]) == "Didovets":
        return "Hello friend"
    else:
        return (array[random_thing])

    #return (array[random_thing]) + " Hello, world!"


### Start flask
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)