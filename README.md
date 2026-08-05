# 🏥 Health Risk Prediction System

## 📌 Project Overview

The **Health Risk Prediction System** is a Machine Learning application that predicts a patient's **health risk level (Low, Medium, or High)** based on medical and lifestyle information.

The project demonstrates a complete Machine Learning workflow, including data analysis, preprocessing, model training, evaluation, and deployment through an interactive dashboard.

---

# 🚀 Features

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Missing Value Handling
* Categorical Feature Encoding
* Feature Scaling
* Logistic Regression Model
* Model Evaluation
* Health Risk Prediction
* Interactive Streamlit Dashboard

---

# 📂 Project Structure

```text
Health-Risk-Prediction/

│── app.py
│── train_model.py
│── eda.py
│── health_data.csv
│── health_risk_model.pkl
│── requirements.txt
│── README.md
```

---

# 📊 Dataset

The dataset contains patient healthcare information.

### Features

| Feature           | Description                |
| ----------------- | -------------------------- |
| Age               | Patient age                |
| Gender            | Male/Female                |
| BMI               | Body Mass Index            |
| BloodPressure     | Blood pressure             |
| Cholesterol       | Cholesterol level          |
| Glucose           | Blood glucose level        |
| Smoking           | Smoking status             |
| Exercise          | Weekly exercise frequency  |
| Diabetes          | Diabetes status            |
| HeartDisease      | Heart disease status       |
| AnnualMedicalCost | Annual medical expenditure |

### Target Variable

* **RiskLevel**

  * Low
  * Medium
  * High

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Streamlit
* Joblib

---

# 📈 Exploratory Data Analysis

The project includes:

* Dataset overview
* Statistical summary
* Missing value analysis
* Duplicate detection
* Correlation heatmap
* Histograms
* Boxplots
* Count plots
* Outlier detection
* Distribution analysis

---

# 🤖 Machine Learning Pipeline

1. Load dataset
2. Handle missing values
3. Encode categorical variables
4. Scale numerical features
5. Split data into training and testing sets
6. Train Logistic Regression model
7. Evaluate model
8. Save trained model

---

# 📊 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# 💻 Dashboard

The Streamlit dashboard provides:

* Dataset preview
* Statistical summary
* Visualizations
* Health risk prediction
* Project information

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Health-Risk-Prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📷 Dashboard Preview

You can add screenshots of your dashboard here after deployment.

---

# 🔮 Future Improvements

* Random Forest and XGBoost models
* Hyperparameter tuning
* Feature importance visualization
* SHAP explainability
* Model comparison dashboard
* Real-time prediction API
* Cloud deployment
* Authentication for users

---

# 👨‍💻 Author

**Manish Parihar**

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
