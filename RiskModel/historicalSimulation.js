// Historical Simulation
function simulatePortfolioReturnsHistorical(assets, weights, returnsMatrix) {
  // Simulate portfolio returns based on historical data
  const portfolioReturns = [];

  const n = assets.length;
  const numObservations = returnsMatrix.length;

  for (let i = 0; i < numObservations; i++) {
    let portfolioReturn = 0;
    for (let j = 0; j < n; j++) {
      portfolioReturn += weights[j] * returnsMatrix[i][j];
    }
    portfolioReturns.push(portfolioReturn);
  }

  return portfolioReturns;
}
