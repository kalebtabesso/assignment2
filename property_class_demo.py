class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Radius: {circle.radius}")
    print(f"Area: {circle.area}")
    print(f"Circumference: {circle.circumference}")

    circle.radius = 10
    print(f"New radius: {circle.radius}")
    print(f"New area: {circle.area}")
    print(f"New circumference: {circle.circumference}")
