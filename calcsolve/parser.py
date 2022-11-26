from utils import Utils



""" Methods to parse the given input.

	Parses numbers, symbols and variables.

	Returns a tree of parsed data.

"""

class Parser:

	def __init__(self, data):

		self.data = data 



	def parse_variables(self):


		""" 
			Parses the variable in the given input equation.
		"""

		data = self.data
		utils = Utils()

		alphabetArray = utils.create_alphabet_array()

		variables = [x for x in data if ord(x) in alphabetArray]

		return variables



	def parse_symbols(self):


		"""
			Parses the symbols in the given input equation.
		"""

		data = self.data
		utils = Utils()

		symbolArray = utils.create_symbol_array()

		symbols = [x for x in data if ord(x) in symbolArray]

		return symbols


	def parse_numbers(self):


		"""
			Parses the numbers in the given input equation.
		"""

		data = self.data
		utils = Utils()

		digitsArray = utils.create_digits_array()

		digits = [x for x in data if x in digitsArray]

		return digits




# parse = Parser("3x^2 + 2x")
# print(parse.parse_numbers())




