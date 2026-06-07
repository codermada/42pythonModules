#! /usr/bin/env python3


class TemperatureError(Exception):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        if self.value < 0:
            return f"{self.value}°C is too cold for plants (min 0°C)"
        elif self.value > 40:
            return f"{self.value}°C is too hot for plants (max 40°C)"
        return f"{self.value}°C is an invalid temperature for plants"


def check_temperature(temp: int) -> None:
    if temp < 0 or temp > 40:
        raise TemperatureError(temp)


def input_temperature(temp_str: str) -> int:
    res = 0
    try:
        res = int(temp_str)
        check_temperature(res)
        return res
    except ValueError as e:
        raise Exception(str(e))


def ft_first_exception() -> None:
    inputs = ["25", "abc"]
    print()
    for data in inputs:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print()
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print()


def test_temperature() -> None:
    inputs = ["100", "-50"]
    print()
    for data in inputs:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
            print()
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print()


def ft_raise_exception() -> None:
    ft_first_exception()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    ft_raise_exception()
    print("=== End of Program ===")
