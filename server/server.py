from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()  # Populate locations to the frontend
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    city = request.form['city']
    POSTED_BY = int(request.form['POSTED_BY'])
    UNDER_CONSTRUCTION = int(request.form['UNDER_CONSTRUCTION'])
    RERA = int(request.form['RERA'])
    BHK_NO = int(request.form['BHK_NO'])
    SQUARE_FT = float(request.form['SQUARE_FT'])

    response = jsonify({
        # populate the estimated price to the frontend
        'estimated_price': util.get_estimated_price(city, POSTED_BY, UNDER_CONSTRUCTION, RERA, BHK_NO, SQUARE_FT)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
