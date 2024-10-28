from greedy_algorithm import greedy_algorithm
from dynamic_programming import dynamic_programming
from menu import Menu

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    menu = Menu(items)
    budget = 100

    greedy_items, greedy_calories = greedy_algorithm(menu, budget)
    print("Greedy Selection:")
    print(f"Items selected: {greedy_items}")
    print(f"Total Calories: {greedy_calories}\n")

    dp_items, dp_calories = dynamic_programming(menu, budget)
    print("Dynamic Programming Selection:")
    print(f"Items selected: {dp_items}")
    print(f"Total Calories: {dp_calories}")

if __name__ == "__main__":
    main()