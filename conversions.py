# Moises Perez
# Week 6 – Testing and Refactoring
# ===========================================================
# PART I: Placeholder functions (TDD – fail first)
# ===========================================================

def convertCelsiusToKelvin(celsius):
    """Placeholder: Celsius → Kelvin"""
    return 0.0   # placeholder for Part I


def convertCelsiusToFahrenheit(celsius):
    """Placeholder: Celsius → Fahrenheit"""
    return 0.0   # placeholder for Part I


# ===========================================================
# PART II: Implemented Celsius Conversion Functions (Make Tests Pass)
# ===========================================================

def convertCelsiusToKelvin_fixed(celsius):
    """
    Converts a Celsius temperature to Kelvin.
    Formula: K = °C + 273.15
    """
    return celsius + 273.15


def convertCelsiusToFahrenheit_fixed(celsius):
    """
    Converts a Celsius temperature to Fahrenheit.
    Formula: °F = (°C × 9/5) + 32
    """
    return (celsius * 9/5) + 32


# ===========================================================
# PART III: Additional Conversions (Fahrenheit ↔ Kelvin ↔ Celsius)
# ===========================================================
# These were developed after writing and running tests that
# initially failed, then corrected here to complete the six
# temperature conversion functions.
# ===========================================================

def convertFahrenheitToCelsius_fixed(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: °C = (°F − 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9


def convertFahrenheitToKelvin_fixed(fahrenheit):
    """
    Converts Fahrenheit to Kelvin.
    Formula: K = (°F + 459.67) × 5/9
    """
    return (fahrenheit + 459.67) * 5/9


def convertKelvinToCelsius_fixed(kelvin):
    """
    Converts Kelvin to Celsius.
    Formula: °C = K − 273.15
    """
    return kelvin - 273.15


def convertKelvinToFahrenheit_fixed(kelvin):
    """
    Converts Kelvin to Fahrenheit.
    Formula: °F = (K × 9/5) − 459.67
    """
    return (kelvin * 9/5) - 459.67
