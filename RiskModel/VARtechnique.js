// Variance-Covariance Approach
function calculatePortfolioRiskVarianceCovariance(assets, weights, covarianceMatrix) {
  // Calculate the portfolio variance using the variance-covariance approach
  let portfolioVariance = 0;
  const n = assets.length;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      portfolioVariance += weights[i] * weights[j] * covarianceMatrix[i][j];
    }
  }

  return portfolioVariance;
}

