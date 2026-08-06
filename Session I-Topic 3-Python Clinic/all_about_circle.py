import numpy as np

def area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return np.pi*radius**2


def circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    # TODO: Implement the function with safeguard of negative radius
    #       to calculate the circumference of a circle given its radius.
    # Hint: you may refer to code above; before implementation, remove "pass" below
    pass


def plot_circle(radius):
    """Plot a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.xlim(-radius - 1, radius + 1)
    plt.ylim(-radius - 1, radius + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Circle with radius {radius}")
    plt.grid()
    plt.show()