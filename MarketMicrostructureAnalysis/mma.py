import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load high-frequency trading data
data = pd.read_csv('trading_data.csv')

# Order Flow Analysis
buy_orders = data[data['Order Type'] == 'Buy']
sell_orders = data[data['Order Type'] == 'Sell']
buy_order_sizes = buy_orders['Order Size'].values
sell_order_sizes = sell_orders['Order Size'].values
buy_order_arrivals = buy_orders['Order Arrival Time'].values
sell_order_arrivals = sell_orders['Order Arrival Time'].values
large_orders = data[data['Order Size'] > 1000]
large_order_impact = large_orders['Price Impact'].values

# Price Discovery Analysis
bid_ask_spreads = data['Bid-Ask Spread'].values
price_impact = data['Price Impact'].values
market_depth = data['Market Depth'].values
order_book_dynamics = data['Order Book Dynamics'].values

# Market Liquidity Analysis
trading_volumes = data['Trading Volume'].values
order_book_depth = data['Order Book Depth'].values
market_impact_costs = data['Market Impact Costs'].values

# Market Impact Analysis
large_trade_impact = data[data['Order Size'] > 1000]['Price Impact'].values
trading_strategy_effectiveness = data['Trading Strategy Effectiveness'].values

# Market Structure Analysis
market_regulations = data['Market Regulations'].values
trading_rules = data['Trading Rules'].values
order_matching_algorithms = data['Order Matching Algorithms'].values
market_fragmentation = data['Market Fragmentation'].values

# High-Frequency Trading Analysis
order_routing_algorithms = data['Order Routing Algorithms'].values
latency_arbitrage = data['Latency Arbitrage'].values
market_making_strategies = data['Market Making Strategies'].values
hft_impact_on_liquidity = data[data['Trader Type'] == 'HFT']['Liquidity'].values

# Plot the results
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs[0, 0].hist(buy_order_sizes, bins=50, alpha=0.5, label='Buy Orders')
axs[0, 0].hist(sell_order_sizes, bins=50, alpha=0.5, label='Sell Orders')
axs[0, 0].set_xlabel('Order Size')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].legend()
axs[0, 1].scatter(buy_order_arrivals, buy_order_sizes, alpha=0.5, label='Buy Orders')
axs[0, 1].scatter(sell_order_arrivals, sell_order_sizes, alpha=0.5, label='Sell Orders')
axs[0, 1].set_xlabel('Order Arrival Time')
axs[0, 1].set_ylabel('Order Size')
axs[0, 1].legend()
axs[0, 2].hist(large_order_impact, bins=50, alpha=0.5)
axs[0, 2].set_xlabel('Price Impact')
axs[0, 2].set_ylabel('Frequency')
axs[1, 0].scatter(bid_ask_spreads, price_impact, alpha=0.5)
axs[1, 0].set_xlabel('Bid-Ask Spread')
axs[1, 0].set_ylabel('Price Impact')
axs[1, 1].scatter(market_depth, order_book_dynamics, alpha=0.5)
axs[1, 1].set_xlabel('Market Depth')
axs[1, 1].set_ylabel('Order Book Dynamics')
axs[1, 2].scatter(trading_volumes, order_book_depth, alpha=0.5)
axs[1, 2].set_xlabel('Trading Volume')
axs[1, 2].set_ylabel('Order Book Depth')
plt.tight_layout()
plt.show()
