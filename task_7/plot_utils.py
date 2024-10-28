import matplotlib.pyplot as plt

def plot_probabilities(probabilities: dict) -> None:
    """
    Plots the probabilities of each possible sum from the dice rolls.

    Parameters:
        probabilities (dict): A dictionary with possible sums as keys and their probabilities as values.
    """
    sums = list(range(2, 13))
    prob_values = [probabilities.get(sum_, 0) for sum_ in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, prob_values, color='skyblue', edgecolor='black')
    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Dice Sums (Monte Carlo Simulation)")
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
