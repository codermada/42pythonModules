#! /usr/bin/env python3
def ft_garden_intro(plant: str, height: float, age: int) -> None:
    print(f"Plant: {plant}")
    print(f"Height: {height} cm")
    print(f"Age: {age} days\n")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_intro("Rose", 25, 30)
    print("=== End of Program ===")
