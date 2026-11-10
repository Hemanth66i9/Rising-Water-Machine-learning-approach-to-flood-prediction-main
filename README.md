# Raising Water: A Machine Learning Approach to Flood Prediction

An intelligent, ML-powered web application that predicts the likelihood of flooding in a region using historical climate and rainfall data — enabling early warnings and proactive disaster preparedness.

---

# Overview

Floods are among the most destructive natural disasters, causing severe damage to life, property, and infrastructure. Traditional flood forecasting methods rely heavily on manual observation and complex hydrological simulations, which are often slow, resource-intensive, and difficult to scale.

**Raising Water** takes a data-driven approach instead. It uses historical climatic indicators — cloud cover, annual rainfall, and seasonal rainfall patterns (Jan–Feb, Mar–May, Jun–Sep) — to train machine learning models that classify whether flood conditions are likely to occur. The best-performing model is deployed behind a simple Flask web interface, so users can enter environmental parameters and get an instant, easy-to-understand prediction: **Flood Likely** or **Flood Not Likely**.

---

# Problem Statement

Accurately predicting flood events is challenging due to the variability of climatic and rainfall patterns, and most existing systems depend heavily on historical data alone, struggle with non-linear climate relationships, or require expensive real-time sensor infrastructure. This project addresses that gap with a lightweight, interpretable, and easily deployable ML-based prediction system that works with just a handful of key environmental features.

---

# Objectives

- Build a machine learning model that accurately predicts flood occurrence from climate and rainfall features.
- Perform thorough exploratory data analysis (EDA), handling missing values and outliers to ensure clean input data.
- Provide a simple, user-friendly web interface for real-time predictions.
- Support disaster management authorities, farmers, and local communities with actionable, early flood-risk insights.

---

# Key Features

-  **Real-time flood prediction** through a clean Flask web interface
-  **Multi-model comparison** — Decision Tree, Random Forest, KNN, and XGBoost, evaluated side by side
-  **Robust preprocessing pipeline** — median imputation for missing values, outlier capping, and feature scaling with `StandardScaler`
-  **Visual feedback** — intuitive Flood / No Flood result pages with supporting imagery
-  **Rigorous evaluation** — accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC
-  **Model persistence** — trained model and scaler serialized with `joblib` for instant reuse without retraining

---

# Methodology

1. **Data Collection** – Historical climate and rainfall dataset sourced from Kaggle, containing cloud cover, annual and seasonal rainfall, and a binary flood/no-flood label.
2. **Exploratory Data Analysis** – Distribution plots, boxplots, and correlation heatmaps to identify the most relevant features.
3. **Data Preprocessing** – Missing value imputation (median), outlier treatment (capping via IQR), and feature scaling (`StandardScaler`).
4. **Model Training** – Decision Tree, Random Forest, KNN, and XGBoost classifiers trained on a 75:25 train-test split.
5. **Model Evaluation** – Compared using accuracy, precision, recall, F1-score, and ROC-AUC; best model selected and saved.
6. **Deployment** – Best model integrated into a Flask web app for real-time, interactive predictions.

---

# System Architecture

```
Environmental Data → Data Preprocessing → ML Model (Decision Tree) → Flask Web App → Prediction Output
```

The system follows a three-layer design:
- **Data Layer** – Collection and preparation of rainfall and climate data
- **Processing & Model Layer** – EDA, preprocessing, model training, and evaluation
- **Application & Presentation Layer** – Flask-based web interface for user interaction

---

#  Tech Stack

| Category | Tools / Libraries |
|---|---|
| **Language** | Python 3.11 |
| **Web Framework** | Flask |
| **ML Libraries** | Scikit-learn, XGBoost |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Model Persistence** | Joblib |
| **IDE** | Visual Studio Code |

---

# Project Structure

```
Rising-Water-Machine-learning-approach-to-flood-prediction/
│
├── static/                 # CSS, images, and static assets
├── templates/               # HTML templates (Home, Predict, Result)
├── model/                   # Saved model and scaler (.pkl files)
├── flood_dataset.xlsx       # Training dataset
├── train_model.py           # Data preprocessing + model training script
├── app.py                   # Flask application entry point
├── requirements.txt         # Python dependencies
└── README.md                 # Project documentation
```

---

# Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hemanth66i9/Rising-Water-Machine-learning-approach-to-flood-prediction-main.git
   cd Rising-Water-Machine-learning-approach-to-flood-prediction
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000/` in your browser.

---

# Model Performance

Four models were trained and compared on the same preprocessed dataset:

| Model | Highlights |
|---|---|
| **Decision Tree** | Interpretable, rule-based, easy to visualize |
| **Random Forest** | Reduced overfitting, higher stability and accuracy |
| **KNN** | Captures local patterns, sensitive to scaling |
| **XGBoost** | Highest predictive performance on non-linear patterns |

The Decision Tree model was ultimately selected for deployment due to its strong balance of accuracy and interpretability — an important factor for building trust with disaster management stakeholders.

---

# Future Enhancements

- Real-time data ingestion from IoT sensors and weather APIs
- GIS-based map visualization of high-risk flood zones
- Integration of deep learning models (e.g., LSTM) for time-series rainfall forecasting
- Mobile application for instant public flood alerts

---

# Contributors

- Karanki Yaswanth Kumar
- Nerusu Dindima Sai Tejaswini
- Pagadala Jayanth Raghavendra
- Pathan Zaheer Khan
- Tungana Hemanth Kumar

**Under the guidance of:** Mr. Ch S Chandra Mouli, Assistant Professor, Dept. of CSE
**Institution:** Kallam Haranadhareddy Institute of Technology (Autonomous), Guntur

---

# License

This project was developed as part of an academic Industrial Internship Project (2025–2026). Feel free to fork and build upon it for educational or research purposes.
