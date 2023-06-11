import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('fraud_data.csv')

# Preprocess the data
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))

# Train the fraud detection model
model = IsolationForest(contamination=0.01)  # 1% of the data is assumed to be fraud
model.fit(data[['Amount', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']])

# Predict fraud labels
data['Fraud'] = model.predict(data[['Amount', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']])

# Identify and report potential fraud cases
potential_fraud = data[data['Fraud'] == -1]
potential_fraud.to_csv('potential_fraud.csv', index=False)