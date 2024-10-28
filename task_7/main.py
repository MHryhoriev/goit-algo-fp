from roll_simulation import roll_dice_simulation
from plot_utils import plot_probabilities
from table_utils import print_probabilities_table

def main():
    # Run the simulation
    num_rolls = 100000  # Adjust for accuracy
    probabilities = roll_dice_simulation(num_rolls)

    # Display the table of probabilities
    print_probabilities_table(probabilities)

    # Plot the probabilities
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()