from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model
model = joblib.load('stroke_prediction_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        
        # Convert to DataFrame with correct feature order
        features = [
            'gender', 'age', 'hypertension', 'heart_disease', 
            'ever_married', 'work_type', 'Residence_type', 
            'avg_glucose_level', 'bmi', 'smoking_status'
        ]
        input_data = pd.DataFrame([data], columns=features)
        
        # Make prediction
        probability = model.predict_proba(input_data)[0, 1]
        
        # Determine risk level
        if probability >= 0.7:
            risk = "High"
        elif probability >= 0.4:
            risk = "Medium"
        else:
            risk = "Low"
        
        return jsonify({
            'probability': float(probability),
            'risk_level': risk,
            'interpretation': f"{risk} risk of stroke"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
