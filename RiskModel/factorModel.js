// Factor Models
function calculatePortfolioRiskFactorModel(assets, weights, factorExposures, factorRiskPremiums) {
  // Calculate portfolio risk using a factor model
  let portfolioRisk = 0;
  const n = assets.length;
  const numFactors = factorExposures[0].length;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < numFactors; j++) {
      portfolioRisk += weights[i] * weights[j] * factorExposures[i][j] * factorRiskPremiums[j];
    }
  }

  return portfolioRisk;
}
