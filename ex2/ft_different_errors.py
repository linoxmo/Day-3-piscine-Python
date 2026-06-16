def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        print(int("hello"))
    except ValueError as e:
        print(e)
    print()
    print("Testing operation 1...")
    try:
        print(5 / 0)
    except ZeroDivisionError as e:
        print(e)
    print()
    print("Testing operation 2...")
    try:
        print(int("hello"))
    except ValueError as e:
        print(e)
    print()
    print("Testing operation 3...")
    try:
        f = open("demofile.txt")
        print(f.read())
    except FileNotFoundError as e:
        print(e)
    print()
    print("Testing operation 4...")
    try:
        print(5 + "Hello")  # type:ignore
    except TypeError as e:
        print(e)
    print()
    print("Operation completed successfully")
    print("All error types tested successfully!")
    return


if __name__ == '__main__':
    test_error_types()
