# Импортируем модуль unittest
import unittest

# Создаем класс testmultiply, который будет наследоваться от класса TestCase в модуле unittest 
class TestMultiply(unittest.TestCase):
    # Внутри класса создаем метод test_multiply
	def test_multiply(self):
		# Умножение двух целых чисел
		result = multiply(5, 5)
		self.assertEqual(result, 25)
		
		# Умножение целого числа на отрицательное целое число
		result = multiply(5, -5)
		self.assertEqual(result, -25)
		
		# Умножение отрицательного целого числа на целое число
		result = multiply(-5, 5)
		self.assertEqual(result, -25)
		
		# Умножение двух отрицательных целых чисел
		result = multiply(-5, -5)
		self.assertEqual(result, 25)
		
		# Умножение нуля на ноль
		result = multiply(0, 0)
		self.assertEqual(result, 0)
		
		# Умножение целого числа на ноль
		result = multiply(2, 0)
		self.assertEqual(result, 0)
		
		# Умножение нуля на десятичное число
		result = multiply(0, 2.5)
		self.assertEqual(result, 0)
		
		# Умножение десятичного числа на целое число
		result = multiply(2.5,1)
		self.assertEqual(result, 2.5)
		
		# Умножение двух десятичных чисел
		result = multiply(1.5, 3.5)
		self.assertEqual(result, 5.25)
		
		# Умножение большого целого числа на целое число
		result = multiply(2**10, 2)
		self.assertEqual(result, 2*2**10)
		
		# Умножение целого числа на большое целое число
		result = multiply(2,2**10)
		self.assertEqual(result, 2*2**10)
		
		# Умножение двух больших целых чисел
		result = multiply(10**10, 10**20)
		self.assertEqual(result, 10**30)
		
		
loader = unittest.TestLoader()                      # Создаем экземпляр тестового загрузчика
suite = loader.loadTestsFromTestCase(TestMultiply)  # Загружаем тестовые сценарии из класса testmultiply
runner = unittest.TextTestRunner()                  # Создаем экземпляр текстового запуска тестов
result = runner.run(suite)                          # Создаем экземпляр текстового запуска тестов