class GardenError(Exception):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "The tomato plant is wilting!",
                 msg_1: str = "") -> None:
        super().__init__(f"{msg}  {msg_1}")


class WaterError(GardenError):
    def __init__(self, msg: str = "Not enough water in the tank!",
                 msg_1: str = "") -> None:
        super().__init__(f"{msg} {msg_1}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...\n")

    for error in [PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
    return


if __name__ == '__main__':
    main()
