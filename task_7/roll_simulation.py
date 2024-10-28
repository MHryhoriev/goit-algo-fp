import random
from collections import defaultdict

def roll_dice_simulation(num_rolls: int) -> dict:
    """
    Simulates rolling two dice a specified number of times and calculates the
    probability of each possible sum from 2 to 12.

    Parameters:
        num_rolls (int): Number of times to roll the dice.

    Returns:
        dict: A dictionary where keys are possible sums (2 to 12) and values are their probabilities.
    """
    sum_counts = defaultdict(int)

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1
    
    probabilities = {sum_: count / num_rolls for sum_, count in sum_counts.items()}
    
    return probabilities
