import cvxpy as cp
import numpy as np

def mean_variance_optimization(expected_returns, covariance_matrix, risk_tolerance):
    num_assets = len(expected_returns)
    
    # Define the portfolio weights as optimization variables
    weights = cp.Variable(num_assets)
    
    # Define the objective function (portfolio risk)
    portfolio_risk = cp.quad_form(weights, covariance_matrix)
    
    # Define the constraints
    constraints = [
        cp.sum(weights) == 1,  # Sum of weights is equal to 1 (fully invested)
        weights >= 0  # Weights are non-negative
    ]
    
    # Define the problem and solve
    problem = cp.Problem(cp.Minimize(portfolio_risk), constraints)
    problem.solve()
    
    # Retrieve the optimal weights
    optimal_weights = weights.value
    
    # Calculate the optimal portfolio return
    optimal_return = np.dot(expected_returns, optimal_weights)
    
    return optimal_weights, optimal_return


# Example data
expected_returns = np.array([0.05, 0.07, 0.09])
covariance_matrix = np.array([[0.04, 0.02, 0.01], [0.02, 0.06, 0.03], [0.01, 0.03, 0.05]])
risk_tolerance = 0.1

# Perform mean-variance optimization
optimal_weights, optimal_return = mean_variance_optimization(expected_returns, covariance_matrix, risk_tolerance)

# Print the optimal weights and return
print("Optimal Weights:", optimal_weights)
print("Optimal Return:", optimal_return)


def risk_parity_allocation(covariance_matrix):
    num_assets = covariance_matrix.shape[0]
    
    # Calculate the asset volatilities
    asset_volatilities = np.sqrt(np.diag(covariance_matrix))
    
    # Calculate the risk parity weights
    risk_contribution = 1 / asset_volatilities
    risk_parity_weights = risk_contribution / np.sum(risk_contribution)
    
    return risk_parity_weights


def black_litterman_model(expected_returns, covariance_matrix, market_weights, investor_views, view_confidences):
    tau = 0.1  # Scaling factor for incorporating views
    
    # Calculate the market-implied returns
    market_implied_returns = np.dot(covariance_matrix, market_weights)
    
    # Calculate the combined expected returns
    combined_returns = tau * np.dot(covariance_matrix, market_weights) + np.dot(np.diag(view_confidences), investor_views)
    
    # Calculate the combined covariance matrix
    combined_covariance = tau * covariance_matrix
    
    # Calculate the Black-Litterman weights
    black_litterman_weights = np.linalg.inv(tau * covariance_matrix).dot(combined_returns)
    
    return black_litterman_weights


# Example data
covariance_matrix = np.array([[0.04, 0.02, 0.01], [0.02, 0.06, 0.03], [0.01, 0.03, 0.05]])
market_weights = np.array([0.4, 0.3, 0.3])
expected_returns = np.array([0.05, 0.07, 0.09])
investor_views = np.array([0.02, 0.04, 0.01])
view_confidences = np.array([0.8, 0.6, 0.9])

# Perform risk parity allocation
risk_parity_weights = risk_parity_allocation(covariance_matrix)

# Perform Black-Litterman model
black_litterman_weights = black_litterman_model(expected_returns, covariance_matrix, market_weights, investor_views, view_confidences)

# Print the allocation weights
print("Risk Parity Weights:", risk_parity_weights)
print("Black-Litterman Weights:", black_litterman_weights)



import numpy as np
import pandas as pd

# Factor-based allocation
def factor_based_allocation(factor_data, risk_factor_exposures):
    # Calculate factor scores
    factor_scores = np.dot(factor_data, risk_factor_exposures.T)
    
    # Normalize factor scores
    normalized_factor_scores = factor_scores / np.sum(np.abs(factor_scores), axis=1, keepdims=True)
    
    # Calculate factor-based weights
    factor_based_weights = normalized_factor_scores / np.sum(np.abs(normalized_factor_scores), axis=1, keepdims=True)
    
    return factor_based_weights


# Monte Carlo simulation for portfolio optimization
def monte_carlo_simulation(returns, num_simulations):
    num_assets = returns.shape[1]
    portfolio_weights = np.zeros((num_simulations, num_assets))
    portfolio_returns = np.zeros(num_simulations)
    portfolio_volatility = np.zeros(num_simulations)

    for i in range(num_simulations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        portfolio_weights[i] = weights

        portfolio_return = np.sum(returns.mean() * weights)
        portfolio_volatilty = np.sqrt(np.dot(weights.T, np.dot(returns.cov(), weights)))

        portfolio_returns[i] = portfolio_return
        portfolio_volatility[i] = portfolio_volatilty

    return portfolio_weights, portfolio_returns, portfolio_volatility


# Example data
factor_data = np.array([[0.2, 0.8, 0.5, 0.3],
                       [0.4, 0.2, 0.6, 0.1],
                       [0.6, 0.4, 0.3, 0.9]])
risk_factor_exposures = np.array([[0.5, -0.2],
                                  [0.3, 0.4],
                                  [0.7, 0.1],
                                  [-0.1, 0.6]])
returns = pd.DataFrame([[0.05, 0.04, 0.02],
                        [0.03, 0.06, 0.01],
                        [0.02, 0.01, 0.07],
                        [0.04, 0.02, 0.03]])
num_simulations = 1000

# Perform factor-based allocation
factor_based_weights = factor_based_allocation(factor_data, risk_factor_exposures)

# Perform Monte Carlo simulation
portfolio_weights, portfolio_returns, portfolio_volatility = monte_carlo_simulation(returns, num_simulations)

# Print the allocation weights
print("Factor-Based Weights:")
print(factor_based_weights)

# Print the simulated portfolio weights, returns, and volatility
print("Monte Carlo Simulation:")
for i in range(num_simulations):
    print("Simulation", i+1)
    print("Weights:", portfolio_weights[i])
    print("Return:", portfolio_returns[i])
    print("Volatility:", portfolio_volatility[i])
    print()

    
#To plot the efficient frontier and identify optimal portfolios,
#I need the expected returns and volatility (risk) values for each portfolio. 
import pandas as pd
import matplotlib.pyplot as plt

# Example data
returns = pd.DataFrame([[0.05, 0.04, 0.02],
                        [0.03, 0.06, 0.01],
                        [0.02, 0.01, 0.07],
                        [0.04, 0.02, 0.03]])

# Calculate expected returns and covariance matrix
expected_returns = returns.mean()
cov_matrix = returns.cov()

# Number of portfolios to simulate
num_portfolios = 1000

# Create empty arrays to store portfolio returns, volatilities, and weights
portfolio_returns = np.zeros(num_portfolios)
portfolio_volatility = np.zeros(num_portfolios)
portfolio_weights = np.zeros((num_portfolios, len(returns.columns)))

# Simulate portfolios
for i in range(num_portfolios):
    weights = np.random.random(len(returns.columns))
    weights /= np.sum(weights)
    portfolio_weights[i, :] = weights

    portfolio_returns[i] = np.sum(expected_returns * weights)
    portfolio_volatility[i] = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Plot the efficient frontier
plt.figure(figsize=(10, 6))
plt.scatter(portfolio_volatility, portfolio_returns, marker='o', s=10, alpha=0.5)
plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.grid(True)

# Identify optimal portfolios
# For example, select portfolios with the highest return for a given risk level
max_return = np.max(portfolio_returns)
target_risk = 0.05  # Set the desired risk level

optimal_portfolios = portfolio_weights[portfolio_volatility <= target_risk]
optimal_returns = portfolio_returns[portfolio_volatility <= target_risk]

# Plot the optimal portfolios
plt.scatter(portfolio_volatility[np.isin(portfolio_returns, optimal_returns)],
            optimal_returns,
            marker='o',
            color='red',
            s=50,
            label='Optimal Portfolios')

# Annotate the optimal portfolios with their risk-return values
for i, (volatility, ret) in enumerate(zip(portfolio_volatility[np.isin(portfolio_returns, optimal_returns)],
                                          optimal_returns)):
    plt.annotate(f'Portfolio {i+1}', (volatility, ret), textcoords='offset points', xytext=(5,-5), ha='left')

plt.legend()
plt.show()
    
    
    
