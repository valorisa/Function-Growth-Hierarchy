import unittest
import sys
import os

# Ajoute le chemin du projet au sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
from scripts.compare_growth import calculate_functions

class TestFunctionGrowth(unittest.TestCase):
    def test_calculate_functions(self):
        n = 100
        k = 2
        functions = calculate_functions(n, a=2, k=k)

        self.assertAlmostEqual(functions["ln(n)"], math.log(n), places=5)
        self.assertAlmostEqual(functions[f"√{k}n"], math.sqrt(n), places=5)
        self.assertAlmostEqual(functions["∛n"], n ** (1/3), places=5)
        self.assertEqual(functions["n"], n)
        self.assertEqual(functions["n^2"], n ** 2)

        # Vérifie que 2^n est correctement calculé ou marqué comme trop grand
        power = 2 ** n
        if len(str(power)) > 50:
            self.assertTrue(isinstance(functions["2^n"], str) and "Trop grand" in functions["2^n"])
        else:
            self.assertEqual(functions["2^n"], power)

if __name__ == "__main__":
    unittest.main()
