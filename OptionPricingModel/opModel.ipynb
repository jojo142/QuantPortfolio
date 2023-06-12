# Black-Scholes-Merton:
import numpy as np
from scipy.stats import norm

def black_scholes_merton(S, K, r, T, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        value = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        value = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    return value

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
option_type = 'call'  # Option type: 'call' or 'put'

option_price = black_scholes_merton(S, K, r, T, sigma, option_type)
print("Option price:", option_price)



# Binomial Option Pricing Model (BOPM):

def binomial_option_pricing(S, K, r, T, sigma, steps, option_type):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    prices = np.zeros((steps + 1, steps + 1))
    prices[0, 0] = S
    
    for i in range(1, steps + 1):
        prices[i, 0] = prices[i - 1, 0] * u
        for j in range(1, i + 1):
            prices[i, j] = prices[i - 1, j - 1] * d
    
    option_values = np.zeros((steps + 1, steps + 1))
    if option_type == 'call':
        option_values[:, steps] = np.maximum(0, prices[:, steps] - K)
    elif option_type == 'put':
        option_values[:, steps] = np.maximum(0, K - prices[:, steps])
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            option_values[i, j] = np.exp(-r * dt) * (p * option_values[i + 1, j] + (1 - p) * option_values[i + 1, j + 1])
    
    return option_values[0, 0]

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
steps = 100  # Number of steps in the binomial tree
option_type = 'call'  # Option type: 'call' or 'put'

option_price = binomial_option_pricing(S, K, r, T, sigma, steps, option_type)
print("Option price:", option_price)


#Monte Carlo Simulation:

def monte_carlo_option_pricing(S, K, r, T, sigma, num_simulations, option_type):
    np.random.seed(42)
    dt = T / 252  # Assuming 252 trading days in a year
    S_t = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.randn(num_simulations))
    
    if option_type == 'call':
        payoff = np.maximum(0, S_t - K)
    elif option_type == 'put':
        payoff = np.maximum(0, K - S_t)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    option_price = np.exp(-r * T) * np.mean(payoff)
    return option_price

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
num_simulations = 100000  # Number of Monte Carlo simulations
option_type = 'call'  # Option type: 'call' or 'put'

option_price = monte_carlo_option_pricing(S, K, r, T, sigma, num_simulations, option_type)
print("Option price:", option_price)
