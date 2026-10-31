# 🏡 Real Estate Investment Advisor
### Predicting Property Profitability & Future Value

An end-to-end Machine Learning project that helps users evaluate property investment potential and estimate future property prices using property-related features.

## 🚀 Live Demo

**[Open Real Estate Investment Advisor](https://real-estate-investment-advisors.streamlit.app/)**

## 📌 Project Overview

Real Estate Investment Advisor is a machine learning-based application designed to analyze property information and provide insights into investment potential.

The project solves two machine learning problems:

1. **Classification:** Predicts whether a property is a Good Investment or Not a Good Investment.
2. **Regression:** Estimates the property's price after five years.

Users can enter property details through an interactive Streamlit application and receive predictions from trained machine learning models.

## 🎯 Project Objectives

- Analyze real estate property data.
- Identify factors that influence property prices.
- Predict property investment potential.
- Estimate future property values.
- Compare multiple machine learning algorithms.
- Track model experiments using MLflow.
- Deploy the trained models through Streamlit.

## 📊 Dataset Information

The project uses a dataset containing **500 property records**.

### Features

| Feature | Description |
|---|---|
| Property_ID | Unique property identifier |
| Area_sqft | Property area in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Floors | Number of floors |
| Year_Built | Year the property was built |
| Location_Score | Location quality score |
| School_Score | Nearby school quality score |
| Current_Price | Current property price |

### Target Variables

- `Good_Investment` – Classification target.
- `Price_After_5_Years` – Regression target.

Additional engineered features:
- `Property_Age`
- `Price_Per_Sqft`
- `Appreciation_Rate`

**Note:** The investment classification label is created using the median appreciation rate in the dataset.

## ⚙️ Machine Learning Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Hyperparameter Tuning
10. MLflow Experiment Tracking
11. Model Saving
12. Streamlit Deployment

## 🤖 Machine Learning Models

### Classification Models
- Logistic Regression
- Random Forest Classifier
- Decision Tree Classifier
- Support Vector Machine (SVM)
- Gradient Boosting Classifier
- Extra Trees Classifier
- HistGradientBoosting Classifier

**Selected classification model:** Tuned Logistic Regression.

### Regression Models
- Linear Regression
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor

**Selected regression model:** Linear Regression.

## 📈 Model Performance

### Classification

The tuned Logistic Regression model achieved approximately **72% test accuracy** in the earlier model comparison.

### Regression

The Linear Regression model achieved the following results:

| Evaluation Metric | Result |
|---|---:|
| MAE | 72,625.25 |
| RMSE | 86,609.11 |
| R² Score | 0.8585 |

These results are based on the recorded train-test evaluation.

## 🧪 MLflow Experiment Tracking

MLflow is used to track machine learning experiments.

Logged metrics include:

- Classification Accuracy
- Weighted F1 Score
- Regression MAE
- Regression RMSE
- Regression R² Score

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Experiment Tracking:** MLflow
- **Model Serialization:** Joblib
- **Web Application:** Streamlit
- **Version Control:** Git & GitHub
- **Deployment:** Streamlit Community Cloud

## 📂 Project Structure

```text
Real-Estate-Investment-Advisor-project/
│
├── app.py
├── requirements.txt
├── best_classification_model.joblib
├── best_regression_model.joblib
├── houseprice_data.csv
├── README.md
└── .gitignore
```

*The project may also contain Jupyter notebooks and additional analysis files.*

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/annuverma888/Real-Estate-Investment-Advisor-project.git
```

### 2. Navigate to the project directory

```bash
cd Real-Estate-Investment-Advisor-project
```

### 3. Create a virtual environment

```bash
python -m venv house
```

### 4. Activate the environment

Windows:

```bash
.\house\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open at:

`http://localhost:8501`

## 🔮 Future Improvements

- Integrate real-time property market data.
- Include additional location-based features.
- Improve classification performance with more relevant data.
- Add interactive property price visualizations.
- Provide location-wise investment comparisons.
- Incorporate explainable AI for prediction insights.

## 👩‍💻 Author

**Annu Verma**

- GitHub: [annuverma888](https://github.com/annuverma888)
- LinkedIn: [Annu Verma](https://linkedin.com/in/annu-verma-41a873326)

## ⭐ Support

If you find this project useful, consider giving this repository a star!

---

**Real Estate Investment Advisor — Machine Learning for Smarter Property Investment Decisions.**
