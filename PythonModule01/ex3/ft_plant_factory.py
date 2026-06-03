#! /usr/bin/env python3


class Plant:
    def __init__(self,
                 name: str, height: float, age: float, growth_rate: float):
        self.__name: str = name
        self.__height: float = height
        self.__height_increase: float = 0
        self.__age: int = round(age)
        self.__growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f} cm, {self.__age} days old")

    def grow(self) -> None:
        self.__height = self.__height + self.__growth_rate
        self.__height_increase = self.__height_increase + self.__growth_rate

    def age(self, days: int) -> None:
        for _ in range(days):
            self.grow()
            self.__age = self.__age + 1

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_height_increase(self) -> float:
        return self.__height_increase

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_height(self, height: float) -> None:
        self.__height = height

    def set_age(self, age: int) -> None:
        self.__age = age

    def set_height_increase(self, height_increase: int) -> None:
        self.__height_increase = height_increase


# def ft_plant_growth(plants: list[Plant],
#                     days: int,
#                     height_increase_label: str) -> None:
#     for plant in plants:
#         plant.show()
#         for i in range(days):
#             print(f"=== Day {i + 1} ===")
#             plant.age(1)
#             plant.show()
#         print(f"{height_increase_label}: {plant.get_height_increase()}cm")
#         plant.set_height_increase(0)


def ft_plant_factory(plants_data:
                     list[tuple[str, float, int, float]]) -> list[Plant]:
    result: list[Plant] = []
    for data in plants_data:
        plant: Plant = Plant(*data)
        result.append(plant)
        print("Created: ", end="")
        plant.show()
    return result


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_data: list[tuple[str, float, int, float]] = [
        ("Rose", 25, 30, 0.8),
        ("Sunflower", 80, 45, 0.5),
        ("Cactus", 15, 120, 0.6),
        ("Tulip", 35, 20, 0.7),
        ("Bamboo", 150, 365, 1.2)
    ]
    plants: list[Plant] = ft_plant_factory(plants_data)
    # ft_plant_growth(plants, 7, "Growth this week")
    print("=== End of Program ===")
