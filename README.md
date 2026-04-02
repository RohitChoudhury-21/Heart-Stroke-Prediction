A machine learning-powered REST API that predicts the probability of stroke based on patient health data. Built using Flask and a trained classification model, this API provides real-time risk assessment for healthcare or research applications.

🚀 What This Project Does

This project exposes a /predict API endpoint that:

Accepts patient health data as JSON
Uses a trained ML model (stroke_prediction_model.pkl)
Returns:
Stroke probability
Risk level (Low / Medium / High)
Simple interpretation
💡 Why This Project Is Useful
⚡ Fast and lightweight API for real-time predictions
🧠 Applies machine learning to a real healthcare problem
🔗 Easy integration with frontend apps or other services
📊 Clear risk categorization for better decision-making
Key Features
Pre-trained model using real dataset (stroke_data.csv)
RESTful API with JSON input/output
CORS enabled (ready for frontend integration)
Simple and interpretable output
🛠️ Getting Started
1️⃣ Clone the Repository
git clone <your-repo-url>
cd <your-repo-name>
2️⃣ Install Dependencies

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install required packages:

pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install flask flask-cors joblib pandas numpy
3️⃣ Run the Application
python app.py

Server will start at:

http://localhost:5000
📡 API Usage
Endpoint
POST /predict
Sample Request
{
  "gender": "Male",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 120.5,
  "bmi": 28.3,
  "smoking_status": "never smoked"
}
Sample Response
{
  "probability": 0.32,
  "risk_level": "Low",
  "interpretation": "Low risk of stroke"
}

🆘 Where to Get Help
Check the training notebook: heart_stroke_detection.ipynb
Review dataset: stroke_data.csv
Open an issue in the repository for bugs or feature requests
👥 Maintainers & Contribution
Maintainer
Rohit Choudhury
Contributing

Contributions are welcome! 🎉

To contribute:

Fork the repository
Create a new branch
Make your changes
Submit a pull request
