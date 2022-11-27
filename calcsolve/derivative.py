from .parser import Parser

class Derivative:

	def __init__(self):

		pass


	def derive(self, data):

		final_expression = ""

		parser = Parser()

		tree, order_tree = parser.split_expressions(data)

		for v, exp in enumerate(tree):

			exp_list = parser.create_parsed_list(exp)


			if len(exp_list) > 1:


				d_number = int(exp_list[0]) * int(exp_list[2])
				d_variable = exp_list[1]
				d_exponent = int(exp_list[2]) - 1

				d_list = [str(d_number), d_variable, str(d_exponent), order_tree[v]]

				d_list = self.finalize_expression(d_list)

				
			else:

				d_list = ['0']


			for e in d_list:
					final_expression += e

			final_expression = self.cleanup(final_expression)

		return final_expression



	def finalize_expression(self, exp):


		if exp[2] == '1':
			exp.pop(2)

		elif exp[2] == '0':
			exp.pop(1)
			exp.pop(1)

		else:
			exp.insert(2, '^')

		return exp


	def cleanup(self, exp):

		if exp[-1] == '0':

			exp = exp[:-2]

		return exp


