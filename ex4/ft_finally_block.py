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


def water_plant(plant_name: str) -> None:
    message = f"Caught PlantError: Invalid plant name to water: '{plant_name}'"
    try:
        if not isinstance(plant_name, str):
            raise PlantError("Plant name must be a string")

        if plant_name != plant_name.capitalize():
            raise PlantError(message)
    except PlantError as e:
        print(f"{e}")
        return
    print(f"Watering {plant_name}: [OK] ")


def main() -> None:
    Plant = [
        "Tomato",
        "Lettuce",
        "Carrot",
        "lettuce"
    ]
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    print("Opening watering system")
    for p in Plant:
        water_plant(p)
    print("Closing watering system")
    print("\nCleanup always happens, even with errors!")
    return


if __name__ == '__main__':
    main()
