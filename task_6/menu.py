class MenuItem:
    """
    Represents an item on the menu with cost and calorie information.

    Attributes:
        name (str): The name of the item.
        cost (int): The cost of the item in units.
        calories (int): The calorie count of the item.
    """
    def __init__(self, name, cost, calories) -> None:
        self.name = name
        self.cost = cost
        self.calories = calories

    def __repr__(self) -> str:
        return f"{self.name} (Cost: {self.cost}, Calories: {self.calories})"


class Menu:
    """
    Represents a menu consisting of multiple items.

    Attributes:
        items (List[MenuItem]): List of MenuItem objects available on the menu.
    """
    def __init__(self, items_data) -> None:
        """
        Initializes the Menu with a dictionary of item data.

        Parameters:
            items_data (Dict[str, Dict[str, int]]): A dictionary where keys are item names
            and values are dictionaries with 'cost' and 'calories' keys.
        """
        self.items = [
            MenuItem(name, data["cost"], data["calories"])
            for name, data in items_data.items()
        ]

    def get_items(self) -> list:
        """
        Returns the list of items on the menu.

        Returns:
            List[MenuItem]: List of MenuItem objects.
        """
        return self.items