def climbingStairs(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return climbingStairs(n-1) + climbingStairs(n-2)