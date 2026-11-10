from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('decision_tree_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    # Get form data
    input_features = ['Cloud Cover', 'ANNUAL', 'Jan-Feb', 'Mar-May', 'Jun-Sep']
    data = []
    for feature in input_features:
        value = float(request.form[feature])
        data.append(value)

    # Convert to DataFrame
    df = pd.DataFrame([data], columns=input_features)

    # Scale features
    df_scaled = scaler.transform(df)

    # Make prediction
    pred = model.predict(df_scaled)[0]

    return render_template('result.html', prediction=pred)

if __name__ == '__main__':
    app.run(debug=True)
