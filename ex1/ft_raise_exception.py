class MyError(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        print("Input data is ’25’")
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(e)
    print()
    try:
        print("Input data is ’abc’")
        temp = input_temperature("ab")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(e)
    print()
    try:
        temp = int(input())
        if temp < 0:
            raise MyError("temperature to low")
        if temp > 40:
            raise MyError("temperature to hight")
    except ValueError as e:
        print(e)
    except MyError as e:
        print(e)


if __name__ == '__main__':
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn’t crash!")
