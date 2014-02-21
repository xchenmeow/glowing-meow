from quadratic_formula import solve_quadratic_equation

# w = (w1, w2) - weights
# covariance - matrix
# w' * cov * w = target variance
# s.t. sum(w) = 1
# when w is 3-d, w3 needs to be provided.
# solve for w

def weights_for_target(cov, target_var, rank=2, w3=0):
	'''
	return the weight for risky asset in the vol target problem
	'''
	# check cov is valid?
	if rank == 2:
		a = cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]
		b = 2 * cov[0, 1] - 2 * cov[1, 1]
		c = cov[1, 1] - target_var
		try:
			weights = solve_quadratic_equation(a, b, c)
		except Exception, e:
			weights = None, None
		
		return weights
	elif rank == 3:
		a = cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]
		b = cov[1, 1] * (2 * w3 - 2) - cov[1, 2] * 2 * w3 + cov[0, 2] * 2 * w3 + cov[0, 1] * 2 * (1 - w3)
		c = cov[2, 2] * w3 * w3 + cov[1, 1] * (1 - 2 * w3 + w3 * w3) + 2 * cov[1, 2] * (1 - w3) * w3 - target_var
		return solve_quadratic_equation(a, b, c)


def simple_weight(vol, target_vol):
	# assuming no correlation
	mat = np.array([vol * vol, 0, 0, 0]).reshape(2, 2)
	return weights_for_target(mat, target_vol * target_vol)[0]


def make_simple_weight(target_vol):
	def weight(vol):
		return simple_weight(vol, target_vol)

	return weight


def two_independent_weights(vol1, vol2, target_vol):
	mat = np.array([vol1 * vol1, 0, 0, vol2 * vol2]).reshape(2, 2)
	w1 = weights_for_target(mat, target_vol * target_vol)[0]
	if w1 is not None:
		w2 = 1 - w1
	else:
		# what to do?
		w1 = 0
		w2 = 0
	
	return w1


def make_two_independent_weights(target_vol):
	def weight(vols):
		vol1 = vols[0]
		vol2 = vols[1]
		return two_independent_weights(vol1, vol2, target_vol)

	return weight


if __name__ == '__main__':
	import numpy as np
	# 0.025149139821247755 -0.0012486673696449771 0.00087716130385294725
	mat = np.array([0.025149139821247755, 0, -0.0012486673696449771, 0,
	 0, 0, -0.0012486673696449771, 0, 0.00087716130385294725]).reshape(3, 3)
	# print mat
	# expecting: 0.64359509624261146
	# [0] takes the larger root.
	print weights_for_target(mat, 0.01, rank=3, w3=0.31300042843175779)[0]

	mat = np.array([0.15 * 0.15, 0, 0, 0]).reshape(2, 2)
	# print mat
	# expecting: 0.64359509624261146
	# [0] takes the larger root.
	print weights_for_target(mat, 0.18 * 0.18)[0]
