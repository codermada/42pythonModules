#! /usr/bin/env python3


def garden_operations(operation_number):
    match operation_number:
        case 0:
            int('abc')  # This will raise a ValueError
        case 1:
            t = 1 / 0  # This will raise a ZeroDivisionError
            print(t)
        case 2:
            open('/non/existent/file')  # This will raise
            # a FileNotFoundError
        case 3:
            print("10" + 10)  # This will raise a TypeError
    print("Operation completed successfully")
    return


def test_error_types() -> None:
    for i in [0, 1, 2, 3, 4]:
        print(f"Testing operation {i} ...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()
    print("All error types tested successfully!")


def ft_different_errors() -> None:
    test_error_types()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    ft_different_errors()
    print("=== End of Program ===")
