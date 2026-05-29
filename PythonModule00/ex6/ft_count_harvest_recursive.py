def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def printDay(d: int) -> None:
        if (d == 0):
            return
        printDay(d - 1)
        print(f"Day {d}")
    printDay(days)
    print("Harvest time!")


# if __name__ == "__main__":
#     ft_count_harvest_recursive()
