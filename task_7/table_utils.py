def print_probabilities_table(probabilities: dict) -> None:
    """
    Prints a table of probabilities for each possible sum from the dice rolls.

    Parameters:
        probabilities (dict): A dictionary with possible sums as keys and their probabilities as values.
    """
    print("Sum of Dice | Probability")
    print("-------------------------")
    for sum_ in range(2, 13):
        probability = probabilities.get(sum_, 0)
        print(f"     {sum_:>2}     | {probability:.4f}")
