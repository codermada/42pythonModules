#! /usr/bin/env python3


class Plant:
    def __init__(self,
                 name: str, height: float, age: float, growth_rate: float):
        self._name: str = name
        self._height: float = height
        self._height_increase: float = 0
        self._age: int = round(age)
        self._growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f} cm, {self._age} days old")

    def grow(self) -> None:
        self._height = self._height + self._growth_rate
        self._height_increase = self._height_increase + self._growth_rate

    def age(self, days: int) -> None:
        for _ in range(days):
            self._height = self._height + self._growth_rate
            self._height_increase = self._height_increase + self._growth_rate
            self._age = self._age + 1

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_height_increase(self) -> float:
        return self._height_increase

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> None:
        if (height == self._height):
            print("Height update rejected")
            return
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if (age == self._age):
            print("Age update rejected")
            return
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age = age

    def set_height_increase(self, height_increase: int) -> None:
        self._height_increase = height_increase


def ft_garden_security(plant_data: tuple[str, float, int, float]) -> None:
    plant: Plant = Plant(*plant_data)
    print("Plant created: ", end="")
    plant.show()
    print()
    print(f"Height updated: {plant.get_height()} cm")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days\n")
    plant.set_height(-1)
    plant.set_height(25)
    plant.set_age(-1)
    plant.set_age(30)
    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants_data: list[tuple[str, float, int, float]] = [
        ("Rose", 25, 10, 0.8),
        ("Sunflower", 80, 45, 0.5),
        ("Cactus", 15, 120, 0.6),
        ("Tulip", 35, 20, 0.7),
        ("Bamboo", 150, 365, 1.2)
    ]
    ft_garden_security(plants_data[0])
    print("=== End of Program ===")
