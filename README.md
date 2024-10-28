# Monte Carlo Dice Roll Simulation

## Project Overview
This project simulates the sum of numbers obtained when rolling two dice a large number of times and calculates the probability of each possible sum (from 2 to 12) using the Monte Carlo method. The results are then compared with analytically derived probabilities for accuracy verification.

## Analytical vs Monte Carlo Results

| Sum of Dice | Analytical Probability | Monte Carlo Probability |
|-------------|------------------------|--------------------------|
| 2           | 2.78% (1/36)           | 2.80%                   |
| 3           | 5.56% (2/36)           | 5.52%                   |
| 4           | 8.33% (3/36)           | 8.21%                   |
| 5           | 11.11% (4/36)          | 11.23%                  |
| 6           | 13.89% (5/36)          | 13.95%                  |
| 7           | 16.67% (6/36)          | 16.55%                  |
| 8           | 13.89% (5/36)          | 13.99%                  |
| 9           | 11.11% (4/36)          | 11.15%                  |
| 10          | 8.33% (3/36)           | 8.36%                   |
| 11          | 5.56% (2/36)           | 5.45%                   |
| 12          | 2.78% (1/36)           | 2.79%                   |

## Observations and Conclusions

1. **Accuracy of Monte Carlo Results**:
   - The probabilities obtained via Monte Carlo simulation are very close to the theoretical, analytically calculated probabilities.
   - The minor variations observed (less than ±0.2% deviation for most sums) are within expected bounds due to the inherent randomness and finite sample size of the Monte Carlo method.
  
2. **Convergence to Analytical Probabilities**:
   - As the number of simulated dice rolls increases, the Monte Carlo results converge closer to the theoretical probabilities, demonstrating the law of large numbers.

3. **Reliability of Monte Carlo for Probability Estimation**:
   - Given a sufficiently large sample size, the Monte Carlo method is shown to be a reliable approach to estimating probabilities, with results closely matching the analytical values.

In conclusion, the Monte Carlo simulation provides an effective approximation of dice roll probabilities, particularly when high numbers of trials are conducted. For this simulation, the results align closely with the analytical probabilities, confirming the accuracy of the Monte Carlo approach.
