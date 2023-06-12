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

#Cox-Ross-Rubinstein Model (CRR):
def crr_option_pricing(S, K, r, T, sigma, steps, option_type):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Generate stock price tree
    stock_tree = np.zeros((steps + 1, steps + 1))
    stock_tree[0, 0] = S

    for i in range(1, steps + 1):
        stock_tree[i, 0] = stock_tree[i - 1, 0] * u
        for j in range(1, i + 1):
            stock_tree[i, j] = stock_tree[i - 1, j - 1] * d

    # Generate option value tree
    option_tree = np.zeros((steps + 1, steps + 1))
    option_tree[:, -1] = np.maximum(0, option_type_factor(option_type) * (stock_tree[:, -1] - K))

    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            option_tree[i, j] = np.exp(-r * dt) * (p * option_tree[i + 1, j] + (1 - p) * option_tree[i + 1, j + 1])

    option_price = option_tree[0, 0]
    return option_price

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
steps = 100  # Number of steps in the binomial tree
option_type = 'call'  # Option type: 'call' or 'put'

option_price = crr_option_pricing(S, K, r, T, sigma, steps, option_type)
print("Option price:", option_price)

#Heston Model

import QuantLib as ql

def heston_option_pricing(S, K, r, T, v0, kappa, theta, sigma, rho, option_type):
    # Option parameters
    option_type = ql.Option.Call if option_type == 'call' else ql.Option.Put
    exercise_date = ql.Date(int(T * 365))
    payoff = ql.PlainVanillaPayoff(option_type, K)
    european_exercise = ql.EuropeanExercise(exercise_date)

    # Heston model parameters
    spot_handle = ql.QuoteHandle(ql.SimpleQuote(S))
    risk_free_curve = ql.FlatForward(0, ql.TARGET(), r, ql.Actual365Fixed())
    dividend_yield = ql.FlatForward(0, ql.TARGET(), 0.0, ql.Actual365Fixed())
    volatility_handle = ql.QuoteHandle(ql.SimpleQuote(sigma))
    heston_process = ql.HestonProcess(risk_free_curve, dividend_yield, spot_handle, volatility_handle,
                                      v0, kappa, theta, sigma, rho)

    # Create the Heston model
    heston_model = ql.HestonModel(heston_process)

    # Create the engine for option pricing
    engine = ql.AnalyticHestonEngine(heston_model)

    # Create the option object
    option = ql.VanillaOption(payoff, european_exercise)
    option.setPricingEngine(engine)

    # Calculate option price
    option_price = option.NPV()
    return option_price

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
v0 = 0.1  # Initial volatility
kappa = 0.5  # Mean reversion speed
theta = 0.1  # Long-term volatility
sigma = 0.1  # Volatility of volatility
rho = -0.5  # Correlation between asset price and volatility
option_type = 'call'  # Option type: 'call' or 'put'

option_price = heston_option_pricing(S, K, r, T, v0, kappa, theta, sigma, rho, option_type)
print("Option price:", option_price)

# Trinomial Option Pricing Model (TOPM) using the QuantLib library:
import QuantLib as ql

def trinomial_option_pricing(S, K, r, T, sigma, steps, option_type):
    # Option parameters
    option_type = ql.Option.Call if option_type == 'call' else ql.Option.Put
    exercise_date = ql.Date(int(T * 365))
    payoff = ql.PlainVanillaPayoff(option_type, K)
    european_exercise = ql.EuropeanExercise(exercise_date)

    # Create the trinomial tree
    spot_price = ql.SimpleQuote(S)
    risk_free_curve = ql.FlatForward(0, ql.TARGET(), r, ql.Actual365Fixed())
    volatility_curve = ql.BlackConstantVol(0, ql.TARGET(), sigma, ql.Actual365Fixed())
    process = ql.BlackScholesMertonProcess(ql.QuoteHandle(spot_price), ql.YieldTermStructureHandle(risk_free_curve),
                                           ql.BlackVolTermStructureHandle(volatility_curve))

    engine = ql.BinomialVanillaEngine(process, "crr", steps)
    
    # Create the option object
    option = ql.VanillaOption(payoff, european_exercise)
    option.setPricingEngine(engine)

    # Calculate option price
    option_price = option.NPV()
    return option_price

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
steps = 100  # Number of steps in the trinomial tree
option_type = 'call'  # Option type: 'call' or 'put'

option_price = trinomial_option_pricing(S, K, r, T, sigma, steps, option_type)
print("Option price:", option_price)

#finite difference method for option pricing, specifically the Crank-Nicolson, Explicit, and Implicit methods.

import numpy as np

def finite_difference_option_pricing(S, K, r, T, sigma, S_max, M, N, option_type, method):
    # Option parameters
    dt = T / N
    dS = S_max / M

    # Grid setup
    S_values = np.linspace(0, S_max, M+1)
    V = np.zeros((M+1, N+1))

    # Set initial and boundary conditions
    if option_type == 'call':
        V[:, N] = np.maximum(S_values - K, 0)
        V[0, :] = 0
        V[M, :] = S_max - K * np.exp(-r * (T - np.arange(N+1) * dt))
    else:
        V[:, N] = np.maximum(K - S_values, 0)
        V[0, :] = K * np.exp(-r * (T - np.arange(N+1) * dt))
        V[M, :] = 0

    # Finite Difference method
    for j in range(N-1, -1, -1):
        for i in range(1, M):
            alpha = 0.25 * dt * (sigma**2 * i**2 - r * i)
            beta = -0.5 * dt * (sigma**2 * i**2 + r)
            gamma = 0.25 * dt * (sigma**2 * i**2 + r * i)
            
            if method == 'crank-nicolson':
                V[i, j] = alpha * V[i-1, j+1] + (1 + beta) * V[i, j+1] + gamma * V[i+1, j+1]
            elif method == 'explicit':
                V[i, j] = alpha * V[i-1, j+1] + (1 - 2 * alpha) * V[i, j+1] + gamma * V[i+1, j+1]
            elif method == 'implicit':
                V[i, j] = np.linalg.solve(A, B)
            
        # Boundary conditions at S = 0 and S = S_max
        if option_type == 'call':
            V[0, j] = 0
            V[M, j] = S_max - K * np.exp(-r * (T - j * dt))
        else:
            V[0, j] = K * np.exp(-r * (T - j * dt))
            V[M, j] = 0
    
    option_price = np.interp(S, S_values, V[:, 0])
    return option_price

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
r = 0.05  # Risk-free interest rate
T = 1  # Time to expiration (in years)
sigma = 0.2  # Volatility
S_max = 200  # Maximum asset price for grid
M = 100  # Number of asset price steps
N = 1000  # Number of time steps
option_type = 'call'  # Option type: 'call' or 'put'
method = 'crank-nicolson'  # Finite difference method: 'crank-nicolson', 'explicit', or 'implicit'

option_price = finite_difference

