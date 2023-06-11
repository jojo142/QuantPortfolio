# Import the necessary libraries
import pandas as pd
from fbprophet import Prophet

# Load the time series data into a Pandas DataFrame
data = pd.read_csv('data.csv')

# Prepare the data for Prophet
df = pd.DataFrame()
df['ds'] = pd.to_datetime(data['date_column'])
df['y'] = data['target_variable']

# Create and fit the Prophet model
model = Prophet()
model.fit(df)

# Generate future dates for forecasting
future = model.make_future_dataframe(periods=365)  # Forecast for the next 365 days

# Perform the forecasting
forecast = model.predict(future)

# Extract the forecasted values
forecasted_values = forecast[['ds', 'yhat']]

# Print the forecasted values
print(forecasted_values)
