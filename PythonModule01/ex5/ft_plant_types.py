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
            self.grow()
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


class Flower(Plant):
    def __init__(self,
                 name: str, height: float,
                 age: float, growth_rate: float, color: str):
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color.lower()}")
        if (self._is_blooming):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self, noise: bool, reverse: bool) -> None:
        if (noise and not reverse):
            print(f"[asking the {self._name.lower()} to bloom]")
        if reverse:
            self._is_blooming = False
        else:
            self._is_blooming = True

    def get_color(self) -> str:
        return self._color

    def get_is_blooming(self):
        return self._is_blooming


class Tree(Plant):
    def __init__(self,
                 name: str, height: float,
                 age: float, growth_rate: float, trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._is_producing_shade = False

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f} cm")

    def produce_shade(self, noise: bool, reverse: bool) -> None:
        if (noise and not reverse):
            print(f"[asking the {self._name.lower()} to produce shade]")
        if reverse:
            self._is_producing_shade = False
        else:
            self._is_producing_shade = True

    def get_is_producing_shade(self, noise: bool):
        if (noise):
            if (self._is_producing_shade):
                print(f"Tree {self._name} now produces a shade of", end="")
                print(f" {self._height:.1f} cm long and ", end="")
                print(f"{self._trunk_diameter:.1f} cm wide.")
            else:
                print(f"Tree {self._name} does not produce a shade yet.")
        return self._is_producing_shade


class Vegetable(Plant):
    def __init__(self,
                 name: str, height: float, age: float,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: int):
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, nutritional_value: int) -> None:
        self._nutritional_value = nutritional_value


def ft_plant_types() -> None:
    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10, 0.8, "Red")
    rose.show()
    rose.bloom(True, False)
    rose.show()

    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200, 365, 1.2, 5)
    oak.show()
    oak.produce_shade(True, False)
    oak.get_is_producing_shade(True)

    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5, 10, 2.1, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.set_nutritional_value(20)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
    print("=== End of Program ===")
