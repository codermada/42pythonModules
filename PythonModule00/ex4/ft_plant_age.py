def ft_plant_age() -> None:
    age: int = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
        return
    print("Plant needs more time to grow.")


# if __name__ == "__main__":
#     ft_plant_age()
