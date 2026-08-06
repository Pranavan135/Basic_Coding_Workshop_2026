from all_about_circle import area, circumference, plot_circle

if __name__ == "__main__":
    radius = 5
    print(f"Area of circle with radius {radius}: {area(radius)}")
    print(f"Circumference of circle with radius {radius}: {circumference(radius)}")
    plot_circle(radius)