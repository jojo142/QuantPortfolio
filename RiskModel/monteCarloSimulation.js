// Monte Carlo Simulation
function simulatePortfolioReturnsMonteCarlo(assets, weights, returnsMatrix, numSimulations) {
  // Simulate portfolio returns using Monte Carlo simulation
  const portfolioReturns = [];
  const n = assets.length;
  const numObservations = returnsMatrix.length;

  for (let i = 0; i < numSimulations; i++) {
    let portfolioReturn = 0;

    for (let j = 0; j < n; j++) {
      const randomIndex = Math.floor(Math.random() * numObservations);
      portfolioReturn += weights[j] * returnsMatrix[randomIndex][j];
    }

    portfolioReturns.push(portfolioReturn);
  }

  return portfolioReturns;
}
