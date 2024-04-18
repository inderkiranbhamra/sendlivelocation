from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    if 'longitude' in data and 'latitude' in data:
        longitude = data['longitude']
        latitude = data['latitude']
        # Do something with longitude and latitude, like saving to a database
        print(f"Received location: Longitude - {longitude}, Latitude - {latitude}")
        return jsonify({'message': 'Location received successfully', 'longitude': longitude, 'latitude': latitude}), 200
    else:
        return jsonify({'error': 'Longitude and latitude not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
