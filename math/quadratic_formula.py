import math

class NegativeDiscriminantException(Exception):
	"""
	Negative Discriminant Exception
	"""
	def __init__(self):
		super(NegativeDiscriminantException, self).__init__()


def solve_quadratic_equation(a, b, c):
	d = b * b - 4 * a * c
	if d < 0:
		raise NegativeDiscriminantException
	x1 = (-b + math.sqrt(d)) / (2 * a)
	x2 = (-b - math.sqrt(d)) / (2 * a)
	return x1, x2


if __name__ == '__main__':
	x = solve_quadratic_equation(1, 2, 1)
	print x
	y = solve_quadratic_equation(1, 1, 1)