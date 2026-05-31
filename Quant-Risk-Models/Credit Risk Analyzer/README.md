# 🏦 Credit Risk Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![Risk Analytics](https://img.shields.io/badge/Domain-Credit%20Risk-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A Credit Risk Modeling project that predicts the probability of borrower default using Logistic Regression and estimates Expected Loss (EL) based on credit risk metrics.

The project applies core banking and financial risk concepts such as Probability of Default (PD), Loss Given Default (LGD), and Expected Loss (EL) to assess borrower risk.

---

# 📌 Features

- Credit Risk Modeling using Logistic Regression
- Probability of Default (PD) Prediction
- Expected Loss (EL) Calculation
- Default Distribution Analysis
- FICO Score Risk Analysis
- ROC Curve Evaluation
- Model Performance Metrics
- Interactive Borrower Risk Assessment

---

# 📊 Dataset Features

The model uses the following borrower information:

| Feature | Description |
|----------|-------------|
| customer_id | Unique customer identifier |
| credit_lines_outstanding | Number of active credit lines |
| loan_amt_outstanding | Outstanding loan amount |
| total_debt_outstanding | Total outstanding debt |
| income | Annual income |
| years_employed | Employment duration |
| fico_score | Credit score |
| default | Target variable (0 = No Default, 1 = Default) |

---

# ⚙️ Risk Modeling Framework

The project follows a standard credit risk workflow:

```text
Historical Loan Data
        ↓
Data Preprocessing
        ↓
Feature Scaling
        ↓
Logistic Regression Model
        ↓
Probability of Default (PD)
        ↓
Loss Given Default (LGD)
        ↓
Expected Loss (EL)
```

---

# 📈 Expected Loss Formula

Expected Loss is calculated using:

EL = PD × EAD × LGD

Where:

- PD = Probability of Default
- EAD = Exposure at Default (Outstanding Loan Amount)
- LGD = Loss Given Default

Assumptions:

```text
Recovery Rate = 10%
LGD = 90%
```

---

# 📊 Visualizations

The project generates:

### Default Distribution

- Number of defaulted and non-defaulted borrowers

### FICO Score Distribution

- Comparison of FICO scores between defaulters and non-defaulters

### ROC Curve

- Evaluates model discrimination ability

---

# 🤖 Machine Learning Model

Model Used:

```text
Logistic Regression
```

Preprocessing:

```text
StandardScaler
```

Target Variable:

```text
default
```

---

# 📏 Evaluation Metrics

The model is evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- ROC-AUC Score

These metrics help assess the effectiveness of the default prediction model.

---

# 🧪 Borrower Risk Assessment

The system accepts borrower information and predicts:

### Probability of Default (PD)

Example:

```text
PD = 0.24
```

Meaning:

```text
24% chance of default
```

### Expected Loss (EL)

Example:

```text
Expected Loss = ₹864
```

Meaning:

```text
The lender is expected to lose ₹864 on average from this borrower.
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Matplotlib

---

# 📂 Project Structure

```text
Credit Risk Analysis/
│
├── CreditRiskAnalysis.py
├── Loan Data.csv
├── README.md
│
└── Screenshots/
    ├── default_distribution.png
    ├── fico_score_analysis.png
    └── roc_curve.png
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install pandas scikit-learn matplotlib
```

Run the project:

```bash
python CreditRiskAnalysis.py
```

---

# 🚀 Future Improvements

- Train/Test Split Evaluation
- Feature Importance Analysis
- Risk Segmentation (Low / Medium / High Risk)
- Confusion Matrix Visualization
- Debt-to-Income Ratio Feature Engineering
- Credit Risk Dashboard
- Advanced Models (Random Forest, XGBoost)

---

# 💡 Learning Outcomes

This project demonstrates:

- Credit Risk Analytics
- Probability of Default Modeling
- Expected Loss Estimation
- Financial Risk Assessment
- Machine Learning for Finance
- Data Visualization
- Predictive Modeling

---

# 📜 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

Developed as part of a Quant Risk Models portfolio focused on financial risk analytics, machine learning, and quantitative risk management.
