def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit not in ["packets", "grams", "area"]:
        print("Unknown unit type")
        return
    print(seed_type.capitalize(), end="")
    print(" seeds: ", end="")
    if unit == "area":
        print("covers ", end="")
    print(f"{quantity} ", end="")
    if unit in ["packets", "grams"]:
        if quantity == 1:
            print(unit[:-1], end="")
        else:
            print(unit, end="")
        if unit == "packets":
            print(" available")
        else:
            print(" total")
    else:
        if quantity == 1:
            print("square meter")
        else:
            print("square meters")


# if __name__ == "__main__":
#     ft_seed_inventory("tomato", 15, "packets")
#     ft_seed_inventory("carrot", 8, "grams")
#     ft_seed_inventory("lettuce", 12, "area")
#     ft_seed_inventory("tomato", 1, "packets")
#     ft_seed_inventory("carrot", 1, "grams")
#     ft_seed_inventory("lettuce", 1, "area")
#     ft_seed_inventory("tomato", 0, "packets")
#     ft_seed_inventory("carrot", 0, "grams")
#     ft_seed_inventory("lettuce", 0, "area")
#     ft_seed_inventory("lettuce", 12, "unknown")
