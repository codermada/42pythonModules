#! /usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError as e:
        raise Exception(str(e))


def first_exception() -> None:
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
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    first_exception()
    print("=== End of Program ===")
