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
    if not isinstance(plant_name, str):
        raise PlantError("Plant name must be a string")

    if plant_name != plant_name.capitalize():
        raise PlantError(message)
    print(f"Watering {plant_name}: [OK] ")


def test_watering_system() -> None:
    Plant = [
        "Tomato",
        "Lettuce",
        "Carrot",
        "lettuce",
        "Potato"
    ]
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for p in Plant:
            water_plant(p)
    except PlantError as e:
        print(e)
        return
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")
    return


if __name__ == '__main__':
    test_watering_system()
