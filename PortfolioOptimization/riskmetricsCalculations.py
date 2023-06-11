def calculate_simple_return(beginning_value, ending_value):
    return (ending_value - beginning_value) / beginning_value


def calculate_cagr(beginning_value, ending_value, num_years):
    return ((ending_value / beginning_value) ** (1 / num_years)) - 1


def calculate_total_return(beginning_value, ending_value, income):
    return (ending_value - beginning_value + income) / beginning_value


# Example data
beginning_value = 100
ending_value = 120
num_years = 5
income = 10

# Calculate simple return
simple_return = calculate_simple_return(beginning_value, ending_value)
print("Simple Return:", simple_return)

# Calculate CAGR
cagr = calculate_cagr(beginning_value, ending_value, num_years)
print("CAGR:", cagr)

# Calculate total return
total_return = calculate_total_return(beginning_value, ending_value, income)
print("Total Return:", total_return)



import numpy as np

def calculate_standard_deviation(returns):
    return np.std(returns, ddof=1)


def calculate_beta(asset_returns, market_returns):
    covariance = np.cov(asset_returns, market_returns)[0, 1]
    market_variance = np.var(market_returns, ddof=1)
    return covariance / market_variance


def calculate_sharpe_ratio(asset_return, risk_free_rate, asset_standard_deviation):
    return (asset_return - risk_free_rate) / asset_standard_deviation


def calculate_sortino_ratio(asset_return, risk_free_rate, asset_returns):
    downside_returns = np.minimum(asset_returns - risk_free_rate, 0)
    downside_standard_deviation = np.std(downside_returns, ddof=1)
    return (asset_return - risk_free_rate) / downside_standard_deviation


# Example data
asset_returns = [0.05, 0.02, -0.03, 0.04, 0.01]
market_returns = [0.04, 0.03, 0.02, 0.05, 0.01]
risk_free_rate = 0.02
asset_return = 0.05

# Calculate standard deviation
std_deviation = calculate_standard_deviation(asset_returns)
print("Standard Deviation:", std_deviation)

# Calculate beta
beta = calculate_beta(asset_returns, market_returns)
print("Beta:", beta)

# Calculate Sharpe ratio
sharpe_ratio = calculate_sharpe_ratio(asset_return, risk_free_rate, std_deviation)
print("Sharpe Ratio:", sharpe_ratio)

# Calculate Sortino ratio
sortino_ratio = calculate_sortino_ratio(asset_return, risk_free_rate, asset_returns)
print("Sortino Ratio:", sortino_ratio)

import numpy as np

def calculate_correlation(asset1_returns, asset2_returns):
    covariance = np.cov(asset1_returns, asset2_returns)[0, 1]
    asset1_std_deviation = np.std(asset1_returns, ddof=1)
    asset2_std_deviation = np.std(asset2_returns, ddof=1)
    correlation = covariance / (asset1_std_deviation * asset2_std_deviation)
    return correlation


def calculate_covariance(asset1_returns, asset2_returns):
    asset1_mean_return = np.mean(asset1_returns)
    asset2_mean_return = np.mean(asset2_returns)
    num_observations = len(asset1_returns)
    covariance = np.sum((asset1_returns - asset1_mean_return) * (asset2_returns - asset2_mean_return)) / (num_observations - 1)
    return covariance


# Example data
asset1_returns = [0.05, 0.02, -0.03, 0.04, 0.01]
asset2_returns = [0.04, 0.03, 0.02, 0.05, 0.01]

# Calculate correlation
correlation = calculate_correlation(asset1_returns, asset2_returns)
print("Correlation:", correlation)

# Calculate covariance
covariance = calculate_covariance(asset1_returns, asset2_returns)
print("Covariance:", covariance)



