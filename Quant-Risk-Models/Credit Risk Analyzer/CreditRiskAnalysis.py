import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,roc_curve
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv("Loan Data.csv")

X = df.drop(columns=["default", "customer_id"])
y = df["default"]

df["default"].value_counts().plot(kind="bar")
plt.title("Default Distribution")
plt.xlabel("Default")
plt.ylabel("Number of Customers")
plt.show()

df[df["default"]==0]["fico_score"].hist(alpha=0.5,label="No Default")
df[df["default"]==1]["fico_score"].hist(alpha=0.5,label="Default")
plt.legend()
plt.title("FICO score vs Default")
plt.xlabel("FICO Score")
plt.ylabel("Frequency")
plt.show()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)
y_pred=model.predict(X_scaled)
RECOVERY_RATE = 0.10
LGD = 1 - RECOVERY_RATE

def expected_loss(borrower):
    X_new = pd.DataFrame([borrower])
    X_new_scaled = scaler.transform(X_new)
    pd_value = model.predict_proba(X_new_scaled)[0, 1]
    el = pd_value * borrower["loan_amt_outstanding"] * LGD
    return pd_value, el

# TEST EXAMPLE
credit_lines_outstanding=int(input("Enter Credit Lines Outstanding = "))
loam_amt_outstanding=int(input("Enter loan ammount outstanding = "))
total_debt_outstanding=int(input("Enter total debt outstanding = "))
income=int(input("Enter Income = "))
years_employed=int(input("Years Employed = "))
fico_score=int(input("Enter FICO Score = "))

borrower = {
    "credit_lines_outstanding": credit_lines_outstanding,
    "loan_amt_outstanding": loam_amt_outstanding,
    "total_debt_outstanding": total_debt_outstanding,
    "income": income,
    "years_employed": years_employed,
    "fico_score": fico_score
}

pd_val, el_val = expected_loss(borrower)
print("PD:", pd_val)
print("Expected Loss:", el_val)

# MODEL EVALUATION
print("Accuracy Score = ",accuracy_score(y,y_pred))
print("Precision Score = ",precision_score(y,y_pred))
print("Recall Score = ",recall_score(y,y_pred))
print("F1 Score = ",f1_score(y,y_pred))
y_prob=model.predict_proba(X_scaled)[:,1]
auc = roc_auc_score(y, y_prob)
print("ROC AUC Score =", auc)
fpr, tpr, thresholds = roc_curve(y, y_prob)
plt.figure(figsize=(8,5))
plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
plt.plot([0,1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()