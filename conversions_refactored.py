# Moises Perez
# PART IV – Refactored Conversion System

class ConversionNotPossible(Exception):
    """Raised when trying to convert between incompatible unit types."""
    pass


def convert(fromUnit, toUnit, value):
    """Converts a given value from one unit to another if compatible."""

    # Normalize inputs to lowercase
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    # Define unit categories
    temperature_units = ["celsius", "fahrenheit", "kelvin"]
    distance_units = ["miles", "yards", "meters"]

    # --- Case 1: Converting within the same unit ---
    if fromUnit == toUnit:
        return float(value)

    # --- Case 2: Temperature conversions ---
    if fromUnit in temperature_units and toUnit in temperature_units:
        # Convert all to Celsius first
        if fromUnit == "celsius":
            celsius = value
        elif fromUnit == "fahrenheit":
            celsius = (value - 32) * 5 / 9
        elif fromUnit == "kelvin":
            celsius = value - 273.15

        # Convert Celsius to target unit
        if toUnit == "celsius":
            return float(celsius)
        elif toUnit == "fahrenheit":
            return float((celsius * 9 / 5) + 32)
        elif toUnit == "kelvin":
            return float(celsius + 273.15)

    # --- Case 3: Distance conversions ---
    elif fromUnit in distance_units and toUnit in distance_units:
        # Convert everything to meters first
        if fromUnit == "meters":
            meters = value
        elif fromUnit == "yards":
            meters = value * 0.9144
        elif fromUnit == "miles":
            meters = value * 1609.344

        # Convert from meters to target unit
        if toUnit == "meters":
            return float(meters)
        elif toUnit == "yards":
            return float(meters / 0.9144)
        elif toUnit == "miles":
            return float(meters / 1609.344)

    # --- Case 4: Incompatible conversions ---
    else:
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}.")
