from .utils import Utils

import re



""" Methods to parse the given input.

	Parses numbers, symbols and variables.

	Returns a tree of parsed data.

"""

class Parser:

	def __init__(self):

		pass



	def parse_variables(self, exp):


		""" 
			Parses the variable in the given input equation.
		"""

		data = exp
		utils = Utils()

		alphabetArray = utils.create_alphabet_array()

		variables = [x for x in data if ord(x) in alphabetArray]

		return variables



	# def parse_symbols(self):


	# 	"""
	# 		Parses the symbols in the given input equation.
	# 	"""

	# 	data = self.data
	# 	utils = Utils()

	# 	symbolArray = utils.create_symbol_array()

	# 	symbols = [x for x in data if ord(x) in symbolArray]

	# 	return symbols


	# def parse_numbers(self):


	# 	"""
	# 		Parses the numbers in the given input equation.
	# 	"""

	# 	data = self.data
	# 	utils = Utils()

	# 	digitsArray = utils.create_digits_array()

	# 	digits = [x for x in data if x in digitsArray]

	# 	return digits


	def split_expressions(self, exp):

		exp_order = []

		for e in exp:
			if e == '+' or e == '-':
				exp_order.append(e)

		split_tree = re.split('\+|\-', exp)

		return split_tree, exp_order




	def create_parsed_list(self, exp):

		utils = Utils()

		alphabetArray = utils.create_alphabet_array()


		if utils.present_in_array(alphabetArray, exp):

			exp = utils.modify_expressions(exp)

			variable = self.parse_variables(exp)[0]

			number = exp[:exp.find(variable)]
			exponent = exp[exp.find('^') + 1:]

			tree = [number, variable, exponent]

		else:

			number = exp[0]
			tree = [number]

		return tree









# parse = Parser()
# # print(parse.create_parsed_list("x"))
# print(parse.split_expressions("3x^2-2x+3"))




