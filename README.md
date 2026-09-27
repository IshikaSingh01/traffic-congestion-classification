# 🚦 Traffic Congestion Classification

## 📌 Project Overview

Traffic Congestion Classification is a Machine Learning project that predicts the traffic congestion level based on different traffic, road, and environmental conditions.

The project uses a **Random Forest Classifier** to classify traffic conditions and provides an interactive **Streamlit web application** for making predictions.

## 🎯 Objective

The main objective of this project is to develop a Machine Learning system that can analyze traffic-related parameters and classify the current congestion condition.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook
* Streamlit

## 📊 Dataset

The dataset contains traffic, road, communication, and environmental parameters.

Important features include:

* Average Speed
* Vehicle Density
* Average Waiting Time
* Road Occupancy
* Traffic Flow
* Queue Length
* Average Acceleration
* Signal State
* Incident Level
* Temperature
* Visibility
* Rain Intensity

The target variable is:

`label`

## 🤖 Machine Learning Model

The project uses:

**Random Forest Classifier**

The model is trained using traffic and environmental features and is evaluated using standard classification metrics.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Random Forest Model
   ↓
Cross Validation
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Deployment
```

## 🌐 Streamlit Application

The Streamlit application allows users to enter traffic and environmental conditions and receive a predicted traffic congestion level.

The application also displays prediction probabilities when supported by the trained model.

## 📁 Project Structure

```text
traffic-congestion-classification/
│
├── app.py
├── traffic_congestion.ipynb
├── deploy_model.pkl
├── requirements.txt
├── README.md
│
└── data/
    └── traffic.csv
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/traffic-congestion-classification.git
```

Open the project folder:

```bash
cd traffic-congestion-classification
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📌 Key Features

* Traffic congestion classification
* Random Forest Machine Learning model
* Traffic and environmental input parameters
* Interactive Streamlit interface
* Prediction probability display
* Jupyter Notebook containing the complete ML workflow

## 🚀 Future Improvements

* Real-time traffic data integration
* IoT sensor integration
* Live traffic monitoring
* Real-time dashboard
* Integration with traffic management systems
* Cloud deployment

## 👩‍💻 Author

**Ishika**

AIML Final Year Student

## 📄 License

This project is created for educational and project purposes.
