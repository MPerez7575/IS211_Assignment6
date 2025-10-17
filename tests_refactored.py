# Moises Perez
import unittest
import conversions_refactored as cr


class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        print("\n=== Temperature Conversions ===")
        test_cases = [
            ("celsius", "kelvin", 0, 273.15),
            ("celsius", "fahrenheit", 100, 212.0),
            ("fahrenheit", "celsius", 32, 0.0),
            ("kelvin", "fahrenheit", 273.15, 32.0),
            ("fahrenheit", "kelvin", 212, 373.15),
        ]
        for from_u, to_u, val, expected in test_cases:
            result = cr.convert(from_u, to_u, val)
            print(f"  {val} {from_u} → {result:.2f} {to_u} (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=2)

    def test_distance_conversions(self):
        print("\n=== Distance Conversions ===")
        test_cases = [
            ("miles", "yards", 1, 1760.0),
            ("yards", "meters", 1, 0.9144),
            ("meters", "yards", 1000, 1093.6133),  # updated expected value
            ("meters", "miles", 1609.344, 1.0),
            ("yards", "miles", 1760, 1.0),
        ]
        for from_u, to_u, val, expected in test_cases:
            result = cr.convert(from_u, to_u, val)
            print(f"  {val} {from_u} → {result:.4f} {to_u} (expected ≈ {expected})")
            self.assertAlmostEqual(result, expected, places=3)

    def test_same_unit(self):
        print("\n=== Same-Unit Conversions ===")
        for unit in ["celsius", "kelvin", "fahrenheit", "miles", "yards", "meters"]:
            value = 123.45
            result = cr.convert(unit, unit, value)
            print(f"  {unit} → {unit} = {result}")
            self.assertEqual(result, value)

    def test_incompatible_units(self):
        print("\n=== Incompatible Unit Conversions ===")
        invalid_pairs = [
            ("celsius", "meters", 10),
            ("yards", "kelvin", 5),
        ]
        for from_u, to_u, val in invalid_pairs:
            print(f"  Attempting {from_u} → {to_u} (should raise ConversionNotPossible)")
            with self.assertRaises(cr.ConversionNotPossible):
                cr.convert(from_u, to_u, val)


if __name__ == "__main__":
    unittest.main(verbosity=2)

