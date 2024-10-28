from typing import List, Tuple
from menu import Menu, MenuItem

def dynamic_programming(menu: Menu, budget: int) -> Tuple[List[MenuItem], int]:
    """
    Solves the food selection problem using dynamic programming to maximize calories
    within the budget constraint.

    Parameters:
        menu (Menu): The menu containing available items.
        budget (int): The maximum budget allowed for selection.

    Returns:
        Tuple[List[MenuItem], int]: A tuple containing the list of selected MenuItem objects
        and the total calories of the selection.
    """
    items = menu.get_items()
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):
            if items[i - 1].cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - items[i - 1].cost] + items[i - 1].calories)
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(items[i - 1])
            b -= items[i - 1].cost

    return selected_items[::-1], total_calories