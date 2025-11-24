# Module 4: Testing
import unittest
from corelogic import ProfitCalculator

class TestProfitCalculator(unittest.TestCase):
    def test_basic_calculation(self):
        # 15 acres, Cost=200, Yield=20, Price=50 -> Profit=12000
        result = ProfitCalculator.calculate(15, 200, 20, 50)
        self.assertEqual(result['net_profit'], 12000)

    def test_negative_input(self):
        result = ProfitCalculator.calculate(-15, 200, 20, 50)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()