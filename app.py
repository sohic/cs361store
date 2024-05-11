from flask import Flask, jsonify, request

app = Flask(__name__)

# Variables to store zip code data
zip_code = "98275"
city = "Mukilteo"
state = "WA"


@app.route('/store', methods=['POST'])
def store_zip_data():
    global zip_code, city, state
    data = request.json
    zip_code = data.get('zip_code', zip_code)
    city = data.get('city', city)
    state = data.get('state', state)

    return jsonify({'message': 'Zip code data stored successfully.'}), 201


@app.route('/retrieve', methods=['GET'])
def retrieve_zip_data():
    return jsonify({'zip_code': zip_code, 'city': city, 'state': state}), 200


if __name__ == '__main__':
    app.run(debug=True)