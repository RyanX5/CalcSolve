class Utils:

	def __init__(self):

		pass


	def create_alphabet_array(self):

		""" Used to create an alphabet array.
			Array of values for all alphabets' ASCII values.
		"""

		symbolArray = [91, 92, 93, 94, 95, 96]

		arr = [x for x in range(65, 123) if x not in symbolArray]

		return arr


	def create_symbol_array(self):

		"""
			Used to create an array of math symbols.

		"""

		symbols = "+-/*^e()"

		arr = [ord(x) for x in symbols]

		return arr


	def create_digits_array(self):

		arr = [str(x) for x in range(0, 10)]

		return arr


	def present_in_array(self, arr, target):

		found = False

		for values in target:
			if ord(values) in arr:
				found = True

		return found


	def modify_expressions(self, exp):

		digitArray = self.create_digits_array()

		if '^' not in exp:

			exp = exp + '^' + '1'

		if exp[0] not in digitArray:

			exp = '1' + exp

		return exp



# utils = Utils()
# print(utils.create_digits_array())

