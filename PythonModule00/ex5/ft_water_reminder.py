def ft_water_reminder() -> None:
    days: int = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
        return
    print("Plants are fine.")


# if __name__ == "__main__":
#     ft_water_reminder()
