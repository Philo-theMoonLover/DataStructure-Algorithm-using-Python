# Returns the maximum value that
# can be put in a knapsack of capacity W

def knapSack(W, wt, val, n):
	# Base Case
	if(W == 0 or n == 0):
		return 0

	# If weight of the nth item is more than Knapsack of capacity W,
	# then this item cannot be included in the optimal solution
	if(wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		result = max(val[n-1] + knapSack(W-wt[n-1], wt, val, n),	# included
					knapSack(W, wt, val, n-1))						# not included
		# print('max', result)
		return result

val = [5, 7, 8]
wt = [3, 4, 5]
W = 10
n = len(val)
for i in range(1,4):
	for j in range(1, W+1):
		print(knapSack(j, wt[0:i], val[0:i], i), end='	')
	print()
