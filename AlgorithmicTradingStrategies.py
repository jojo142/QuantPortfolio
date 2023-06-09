### Moving average crossover strategy:
import pandas as pd

# Load historical price data into a DataFrame
df = pd.read_csv('historical_data.csv')  # Replace 'historical_data.csv' with your actual data file

# Calculate the moving averages
df['MA_short'] = df['Close'].rolling(window=10).mean()  # Short-term moving average
df['MA_long'] = df['Close'].rolling(window=30).mean()   # Long-term moving average

# Generate trading signals
df['Signal'] = 0  # Initialize a column for trading signals
df.loc[df['MA_short'] > df['MA_long'], 'Signal'] = 1  # Set signal to 1 for buy signals
df.loc[df['MA_short'] < df['MA_long'], 'Signal'] = -1  # Set signal to -1 for sell signals

# Calculate position changes based on the signals
df['Position'] = df['Signal'].diff()

# Backtest the strategy
initial_capital = 100000  # Initial capital in your account
position = 0  # Initialize position as 0
for index, row in df.iterrows():
    if row['Position'] == 1:  # Buy signal
        if position == 0:
            position = initial_capital / row['Close']
    elif row['Position'] == -1:  # Sell signal
        if position > 0:
            initial_capital = position * row['Close']
            position = 0

# Calculate the final portfolio value
portfolio_value = initial_capital if position == 0 else position * df['Close'].iloc[-1]

print(f"Final Portfolio Value: {portfolio_value:.2f}")

### Mean Reversion Strategy:
import pandas as pd

df = pd.read_csv('historical_data.csv')

# Calculate mean and standard deviation
mean = df['Close'].mean()
std = df['Close'].std()

# Generate trading signals based on deviations from the mean
df['Signal'] = 0
df.loc[df['Close'] > mean + std, 'Signal'] = -1  # Sell signal
df.loc[df['Close'] < mean - std, 'Signal'] = 1  # Buy signal

# Backtest the strategy and calculate portfolio value
# ...

### Breakout Strategy:
import pandas as pd

df = pd.read_csv('historical_data.csv')

# Define breakout threshold and calculate rolling high and low
breakout_threshold = 0.02
df['RollingHigh'] = df['Close'].rolling(window=20).max()
df['RollingLow'] = df['Close'].rolling(window=20).min()

# Generate trading signals based on breakout thresholds
df['Signal'] = 0
df.loc[df['Close'] > df['RollingHigh'] * (1 + breakout_threshold), 'Signal'] = 1  # Buy signal
df.loc[df['Close'] < df['RollingLow'] * (1 - breakout_threshold), 'Signal'] = -1  # Sell signal

# Backtest the strategy and calculate portfolio value
# ...

### MACD Strategy:
import pandas as pd
import talib

df = pd.read_csv('historical_data.csv')

# Calculate MACD and signal line
macd, signal, _ = talib.MACD(df['Close'])

# Generate trading signals based on MACD crossover
df['Signal'] = 0
df.loc[macd > signal, 'Signal'] = 1  # Buy signal
df.loc[macd < signal, 'Signal'] = -1  # Sell signal

# Backtest the strategy and calculate portfolio value
# ...
