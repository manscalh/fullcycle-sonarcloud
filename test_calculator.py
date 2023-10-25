import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_soma(self):
        
        self.assertEqual(calculator.soma(2,2),4)
        
    def test_subtracao(self):
        
        self.assertEqual(calculator.subtracao(5,3),2)
        
    def test_multiplicacao(self):
        
        self.assertEqual(calculator.multiplicacao(2,2),4)
        
    def test_divisao(self):
        
        self.assertEqual(calculator.divisao(4,4),1)
        
        
if __name__ == '__main__':
    unittest.main()