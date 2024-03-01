# fruit_project.py

class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def describe(self):
        return f"A {self.color} {self.name} that tastes {self.taste}."


def main():
    apple = Fruit("apple", "red", "sweet")
    banana = Fruit("banana", "yellow", "sweet")
    orange = Fruit("orange", "orange", "citrusy")

    print(apple.describe())
    print(banana.describe())
    print(orange.describe())


if __name__ == "__main__":
    main()
