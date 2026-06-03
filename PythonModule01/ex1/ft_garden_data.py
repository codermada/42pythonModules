#! /usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data(plants: list[tuple[str, float, int]]) -> None:
    for plant in plants:
        Plant(*plant).show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants: list[tuple[str, float, int]] = [
        ("Rose", 25, 30),
        ("Sunflower", 80, 45),
        ("Cactus", 15, 120)]
    ft_garden_data(plants)
    print("=== End of Program ===")
