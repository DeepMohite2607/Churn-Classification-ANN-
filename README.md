# 🏦 Employee Churn Prediction using Artificial Neural Network (ANN)

## 📌 Overview

Employee attrition is one of the biggest challenges faced by organizations. Predicting whether an employee is likely to leave helps companies take proactive retention measures.

This project uses an **Artificial Neural Network (ANN)** built with **TensorFlow/Keras** to predict whether an employee will leave the company based on various demographic, financial, and employment-related features.

---

## 🚀 Features

* Data preprocessing and cleaning
* Label Encoding & One-Hot Encoding
* Feature Scaling using StandardScaler
* Artificial Neural Network (ANN) model
* Binary Classification (Leave / Stay)
* Model Evaluation using Accuracy
* Prediction on new employee data
* Saved model for future inference

---

## 📂 Project Structure

```text
Churn-Classification-ANN/
│
├── Churn_Modelling.csv              # Dataset
├── experiments.ipynb                # Model training notebook
├── prediction.ipynb                 # Prediction notebook
├── model.h5                         # Trained ANN model
├── scaler.pkl                       # StandardScaler object
├── label_encoder_gender.pkl         # Gender encoder
├── onehot_encoder_geo.pkl           # Geography encoder
├── app.py                           # Streamlit application
├── requirements.txt                 # Required libraries
├── README.md                        # Project documentation
└── LICENSE
```

---

## 📊 Dataset

The dataset contains customer/employee information used to predict churn.

### Features

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary

### Target Variable

| Value | Meaning                  |
| ----- | ------------------------ |
| 0     | Employee/Customer Stays  |
| 1     | Employee/Customer Leaves |

---

## 🧠 Model Architecture

The ANN consists of:

* Input Layer
* Hidden Layer (ReLU)
* Hidden Layer (ReLU)
* Output Layer (Sigmoid)

Activation Functions:

* ReLU
* Sigmoid

Loss Function:

* Binary Crossentropy

Optimizer:

* Adam

Evaluation Metric:

* Accuracy

---

## ⚙️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Streamlit
* Pickle

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Encode Categorical Variables
5. Scale Numerical Features
6. Train-Test Split
7. Build ANN Model
8. Train the Model
9. Evaluate Performance
10. Save Model
11. Predict New Data

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/DeepMohite2607/Churn-Classification-ANN-.git
```

Move into the project directory

```bash
cd Churn-Classification-ANN-
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Train Model

Open

```bash
experiments.ipynb
```

Run all cells.

---

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Model Performance

Evaluation Metrics

* Accuracy
* Loss
* Binary Classification

The ANN learns hidden relationships between employee/customer attributes and churn behavior to make accurate predictions.

---

## 📌 Future Improvements

* Hyperparameter Tuning
* Dropout Regularization
* Batch Normalization
* Cross Validation
* Model Explainability (SHAP/LIME)
* Docker Deployment
* AWS Deployment
* CI/CD Pipeline

---

## 💡 Business Use Cases

* Employee Attrition Prediction
* Customer Churn Prediction
* HR Analytics
* Banking Customer Retention
* Telecom Customer Retention
* Insurance Customer Retention

---

## 📚 Skills Demonstrated

* Deep Learning
* Artificial Neural Networks (ANN)
* TensorFlow & Keras
* Data Preprocessing
* Feature Engineering
* Model Evaluation
* Machine Learning Pipeline
* Streamlit Deployment
* Model Serialization
* Binary Classification

---

## 📸 Sample Prediction

```text
Input:

Age: 42
Gender: Male
Balance: 120000
Tenure: 6
Active Member: Yes

Prediction:

Probability of Leaving: 0.84

Prediction:
Employee is likely to leave the company.
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

## 👨‍💻 Author

**Deep Mohite**

* GitHub: https://github.com/DeepMohite2607
* LinkedIn: *(Add your LinkedIn profile here)*

---

## 📄 License

This project is licensed under the **MIT License**.
