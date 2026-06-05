#! /usr/bin/env python3
from typing_extensions import Self


class Plant:
    def __init__(self,
                 name: str = "Unkwown plant",
                 height: float = 0,
                 age: float = 0,
                 growth_rate: float = 0):
        self._name: str = name
        self._height: float = height
        self._height_increase: float = 0
        self._age: int = round(age)
        self._growth_rate: float = growth_rate
        self._stats = Plant.Stats(0, 0, 0)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f} cm, {self._age} days old")
        self._stats.show_calls += 1

    def grow(self) -> None:
        self._height = self._height + self._growth_rate
        self._height_increase = self._height_increase + self._growth_rate
        self._stats.grow_calls += 1

    def age(self, days: int) -> None:
        for _ in range(days):
            self._height = self._height + self._growth_rate
            self._height_increase = self._height_increase + self._growth_rate
            self._age = self._age + 1
        self._stats.age_calls += 1

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

    @staticmethod
    def is_age_older_than_a_year(days: float) -> bool:
        if (round(days) > 365):
            return True
        return False

    @classmethod
    def new_object(cls) -> Self:
        return cls()

    class Stats:
        def __init__(self, grow_calls, age_calls, show_calls):
            self.grow_calls = grow_calls
            self.age_calls = age_calls
            self.show_calls = show_calls

        def display(self, plant_name: str):
            print(f"[statistics for {plant_name}]")
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def show_statistics(self):
        self._stats.display(self._name)


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

    def get_is_blooming(self) -> bool:
        return self._is_blooming


class Seed(Flower):
    def __init__(self,
                 name: str, height: float,
                 age: float, growth_rate: float, color: str):
        super().__init__(name, height, age, growth_rate, color)
        self._seed_count = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")

    def get_seed_count(self):
        return self._seed_count

    def increment_seed_count_by(self, n: int) -> None:
        if (super().get_is_blooming()):
            self._seed_count += n
        else:
            self._seed_count = 0


class Tree(Plant):
    def __init__(self,
                 name: str, height: float,
                 age: float, growth_rate: float, trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._is_producing_shade = False
        self._stats: Tree.TreeStats = Tree.TreeStats(0, 0, 0)

    class TreeStats(Plant.Stats):
        def __init__(self, grow_calls, age_calls, show_calls):
            super().__init__(grow_calls, age_calls, show_calls)
            self.shade_count = 0

        def display(self, plant_name: str):
            super().display(plant_name)
            print(f" {self.shade_count} shade")

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
        self._stats.shade_count += 1

    def get_is_producing_shade(self, noise: bool):
        if (noise):
            if (self._is_producing_shade):
                print(f"Tree {self._name} now produces a shade of", end="")
                print(f" {self._height:.1f} cm long and ", end="")
                print(f"{self._trunk_diameter:.1f} cm wide.")
            else:
                print(f"Tree {self._name} does not produce a shade yet.")
        return self._is_producing_shade

    def show_statistics(self):
        self._stats.display(self._name)


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


def show_stats(plant: Plant):
    plant.show_statistics()


def ft_garden_analytics() -> None:
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ")
    print(f"{'True' if Plant.is_age_older_than_a_year(30) else 'False'}")
    print("Is 400 days more than a year? -> ")
    print(f"{'True' if Plant.is_age_older_than_a_year(400) else 'False'}")

    print()

    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10, 7, "Red")
    rose.show()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom(False, False)
    rose.show()
    show_stats(rose)

    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200, 365, 1.2, 5)
    oak.show()
    oak.show_statistics()
    oak.produce_shade(True, False)
    oak.get_is_producing_shade(True)
    show_stats(oak)

    print()

    print("=== Seed")
    seed: Seed = Seed("Sunflower", 80, 45, 1.43, "yellow")
    seed.show()
    print(" [make sunflower grow, age and bloom]")
    seed.grow()
    seed.age(20)
    seed.bloom(False, False)
    seed.increment_seed_count_by(42)
    seed.show()
    show_stats(seed)

    print()

    print("=== Anonymous")
    unknown: Plant = Plant.new_object()
    unknown.show()
    show_stats(unknown)

    print()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_garden_analytics()
    print("=== End of Program ===")
