from quadratic_formula import solve_quadratic_equation

# w = (w1, w2) - weights
# covariance - matrix
# w' * cov * w = target variance
# solve for w

def weights_for_target(cov, target_var, rank=2, w3=0):
	# check cov is valid?
	if rank == 2:
		a = cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]
		b = 2 * cov[0, 1] - 2 * cov[1, 1]
		c = cov[1, 1] - target_var
		weights = solve_quadratic_equation(a, b, c)
		return weights
	elif rank == 3:
		a = cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]
		b = cov[1, 1] * (2 * w3 - 2) - cov[1, 2] * 2 * w3 + cov[0, 2] * 2 * w3 + cov[0, 1] * 2 * (1 - w3)
		c = cov[2, 2] * w3 * w3 + cov[1, 1] * (1 - 2 * w3 + w3 * w3) + 2 * cov[1, 2] * (1 - w3) * w3 - target_var
		return solve_quadratic_equation(a, b, c)


if __name__ == '__main__':
	import numpy as np
	# 0.025149139821247755 -0.0012486673696449771 0.00087716130385294725
	mat = np.array([0.025149139821247755, 0, -0.0012486673696449771, 0, 0, 0, -0.0012486673696449771, 0, 0.00087716130385294725]).reshape(3, 3)
	# print mat
	# expecting: 0.64359509624261146
	# [0] takes the larger root.
	print weights_for_target(mat, 0.01, rank=3, w3=0.31300042843175779)[0]
