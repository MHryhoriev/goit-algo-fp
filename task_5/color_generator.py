from typing import List

def generate_color_gradient(start: tuple, end: tuple, n: int) -> List[str]:
    """
    Generate a list of colors in RGB format that create a gradient from a start color to an end color.

    Parameters:
        start (tuple): A tuple representing the RGB values of the starting color.
        end (tuple): A tuple representing the RGB values of the ending color.
        n (int): The number of colors to generate in the gradient.

    Returns:
        List[str]: A list of colors in hex format, representing the gradient.
    """
    colors = []
    for i in range(n):
        r = int(start[0] + (end[0] - start[0]) * (i / (n - 1)))
        g = int(start[1] + (end[1] - start[1]) * (i / (n - 1)))
        b = int(start[2] + (end[2] - start[2]) * (i / (n - 1)))
        colors.append(f'#{r:02x}{g:02x}{b:02x}')  # Convert to hex format
    return colors