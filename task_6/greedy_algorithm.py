from menu import Menu, MenuItem
from typing import List, Tuple

def greedy_algorithm(menu: Menu, budget: int) -> Tuple[List[MenuItem], int]:
    """
    Solves the food selection problem using a greedy algorithm that maximizes calories-to-cost ratio.

    Parameters:
        menu (Menu): The menu containing available items.
        budget (int): The maximum budget allowed for selection.

    Returns:
        Tuple[List[MenuItem], int]: A tuple containing the list of selected MenuItem objects
        and the total calories of the selection.
    """
    sorted_items = sorted(menu.get_items(), key=lambda item: item.calories / item.cost, reverse=True)
    total_calories = 0
    selected_items = []

    for item in sorted_items:
        if budget >= item.cost:
            selected_items.append(item)
            total_calories += item.calories
            budget -= item.cost

    return selected_items, total_calories