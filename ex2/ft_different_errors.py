def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print(int("hello"))
    except ValueError as e:
        print(e)
    print()
    try:
        print(5 / 0)
    except ZeroDivisionError as e:
        print(e)
    print()
    try:
        print(int("hello"))
    except ValueError as e:
        print(e)
    print()
    try:
        f = open("demofile.txt")
        print(f.read())
    except FileNotFoundError as e:
        print(e)
    print()
    try:
        print(5 + "Hello")
    except TypeError as e:
        print(e)
    print()
    print("Operation completed successfully")
    print("All error types tested successfully!")
    return


if __name__ == '__main__':
    test_error_types()
