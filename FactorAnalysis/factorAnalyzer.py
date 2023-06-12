import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler

# Example data
data = pd.DataFrame({
    'Variable1': [1.2, 2.3, 3.1, 4.2, 5.0],
    'Variable2': [0.8, 1.9, 2.7, 3.6, 4.5],
    'Variable3': [1.1, 2.0, 2.9, 3.8, 4.7],
    'Variable4': [0.9, 1.8, 2.6, 3.5, 4.4]
})

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Perform factor analysis
n_factors = 2  # Number of factors to extract
fa = FactorAnalysis(n_components=n_factors, random_state=0)
factor_scores = fa.fit_transform(scaled_data)

# Get factor loadings
factor_loadings = pd.DataFrame(
    fa.components_.T,
    index=data.columns,
    columns=[f'Factor{i+1}' for i in range(n_factors)]
)

# Print factor loadings
print("Factor Loadings:")
print(factor_loadings)

# Get explained variance ratio
explained_variance_ratio = fa.explained_variance_ratio_
print("\nExplained Variance Ratio:")
print(explained_variance_ratio)

# Get factor scores
factor_scores_df = pd.DataFrame(
    factor_scores,
    columns=[f'Factor{i+1}' for i in range(n_factors)]
)
print("\nFactor Scores:")
print(factor_scores_df)


#when i have acquired the csv file

# Step 2: Data Collection
# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Step 3: Data Preprocessing (if needed)
# Clean and preprocess the data as necessary

# Step 4: Choose the Factor Analysis Method
# Initialize the FactorAnalyzer object with the desired method
factor_analyzer = FactorAnalyzer(n_factors=3, method='principal', rotation='varimax')

# Step 6: Perform Factor Extraction
# Fit the factor analysis model to the data
factor_analyzer.fit(data)

# Step 7: Assess Factor Loadings
# Get the factor loadings
factor_loadings = factor_analyzer.loadings_

# Step 8: Perform Rotation (if needed)
# Perform factor rotation
factor_analyzer.rotate()

# Step 9: Interpret and Name Factors
# Get the rotated factor loadings
rotated_loadings = factor_analyzer.loadings_

# Step 10: Assess Model Fit (if applicable)
# Calculate the model fit statistics (if using CFA)

# Step 11: Validate and Refine
# Validate the factor structure and refine as necessary

# Print the factor loadings and rotated loadings
print("Factor Loadings:")
print(factor_loadings)
print("\nRotated Loadings:")
print(rotated_loadings)
