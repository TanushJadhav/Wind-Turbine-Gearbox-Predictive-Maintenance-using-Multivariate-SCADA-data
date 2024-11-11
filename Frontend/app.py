from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from keras.models import model_from_json

app = Flask(__name__, static_url_path='/static')
CORS(app)

file = open('../Model Files/LSTM Model/model.json', 'r')
loaded  = file.read()
file.close()

model = model_from_json(loaded)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if data:
        sel_model = data.get('sel_model')
        temp1 = float(data.get('temp1'))
        temp2 = float(data.get('temp2'))
        temp3 = float(data.get('temp3'))
        temp4 = float(data.get('temp4'))
        temp5 = float(data.get('temp5'))
        temp6 = float(data.get('temp6'))

        print(temp1, temp2, temp3, temp4, temp5, temp6)

        if sel_model == "gear_oil_temp":
            model.load_weights("../Model Files/LSTM Model/Gear oil temperature (°C).csv.h5")
        elif sel_model == "gear_oil_inlet_temp":
            model.load_weights("../Model Files/LSTM Model/Gear oil inlet temperature (°C).csv.h5")
        elif sel_model == "front_bearing_temp":
            model.load_weights("../Model Files/LSTM Model/Front bearing temperature (°C).csv.h5")
        elif sel_model == "rear_bearing_temp":
            model.load_weights("../Model Files/LSTM Model/Rear bearing temperature (°C).csv.h5")
        elif sel_model == "gen_bearing_front_temp":
            model.load_weights("../Model Files/LSTM Model/Generator bearing front temperature (°C).csv.h5")
        elif sel_model == "gen_bearing_rear_temp":
            model.load_weights("../Model Files/LSTM Model/Generator bearing rear temperature (°C).csv.h5")
        elif sel_model == "rotor_bearing_temp":
            model.load_weights("../Model Files/LSTM Model/Rotor bearing temp (°C).csv.h5")
        else:
            model.load_weights("../Model Files/LSTM Model/Stator temperature 1 (°C).csv.h5")

        # prediction = model.predict([[temp1, temp2, temp3, temp4, temp5, temp6]])[0,0]
        prediction = model.predict([[[temp1, temp2, temp3, temp4, temp5, temp6]]])[0,0]
        
        return jsonify({'prediction': float(prediction)})    
    
    return jsonify({'error': 'No data received'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)