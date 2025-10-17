# Moises Perez
import unittest
import conversions


class TestCelsiusConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("\nTesting convertCelsiusToKelvin_fixed:")
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (25.0, 298.15),
            (300.0, 573.15)
        ]
        for celsius, expected in test_cases:
            result = conversions.convertCelsiusToKelvin_fixed(celsius)  # ← fixed version
            print(f"  {celsius} °C → {result} K (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("\nTesting convertCelsiusToFahrenheit_fixed:")
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (25.0, 77.0),
            (300.0, 572.0)
        ]
        for celsius, expected in test_cases:
            result = conversions.convertCelsiusToFahrenheit_fixed(celsius)  # ← fixed version
            print(f"  {celsius} °C → {result} °F (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)

# -----------------------------------------------------------
# PART III: Fahrenheit ↔ Kelvin ↔ Celsius Conversions
# -----------------------------------------------------------

    def test_convertFahrenheitToCelsius(self):
        print("\nTesting convertFahrenheitToCelsius_fixed:")
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (77.0, 25.0),
            (572.0, 300.0)
        ]
        for f, expected in test_cases:
            result = conversions.convertFahrenheitToCelsius_fixed(f)
            print(f"  {f} °F → {result} °C (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)


    def test_convertFahrenheitToKelvin(self):
        print("\nTesting convertFahrenheitToKelvin_fixed:")
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (77.0, 298.15),
            (572.0, 573.15)
        ]
        for f, expected in test_cases:
            result = conversions.convertFahrenheitToKelvin_fixed(f)
            print(f"  {f} °F → {result} K (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)


    def test_convertKelvinToCelsius(self):
        print("\nTesting convertKelvinToCelsius_fixed:")
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (298.15, 25.0),
            (573.15, 300.0)
        ]
        for k, expected in test_cases:
            result = conversions.convertKelvinToCelsius_fixed(k)
            print(f"  {k} K → {result} °C (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)


    def test_convertKelvinToFahrenheit(self):
        print("\nTesting convertKelvinToFahrenheit_fixed:")
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (0.0, -459.67),
            (298.15, 77.0),
            (573.15, 572.0)
        ]
        for k, expected in test_cases:
            result = conversions.convertKelvinToFahrenheit_fixed(k)
            print(f"  {k} K → {result} °F (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
