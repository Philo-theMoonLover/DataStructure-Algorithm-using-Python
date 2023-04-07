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

# Print out the best plan for
def bestPlan(val, n, k, i1, i2, i3):
	if(k == 2):
		while(n != i1*val[0] + i2*val[1]):
			i1 += 1
			if(n < i1*val[0] + i2*val[1]):
				i1 -= 1
				break
		while(n != i1*val[0] + i2*val[1]):
			i2 += 1
			if(n < i1*val[0] + i2*val[1]):
				i1 -= 1
				break
		return[i1, i2, i3]
	if(k == 3):
		while (n != i1 * val[0] + i2 * val[1] + i3*val[2]):
			i1 += 1
			if (n < i1 * val[0] + i2 * val[1] + i3*val[2]):
				i1 -= 1
				break
		while (n != i1 * val[0] + i2 * val[1] + i3*val[2]):
			i2 += 1
			if (n < i1 * val[0] + i2 * val[1] + i3*val[2]):
				i1 -= 1
				break
		while (n != i1 * val[0] + i2 * val[1] + i3*val[2]):
			i2 += 1
			if (n < i1 * val[0] + i2 * val[1] + i3*val[2]):
				i1 -= 1
				break
		return [i1, i2, i3]


val = [5, 7, 8]
wt = [3, 4, 5]
W = 10
n = len(val)
list1 = []
list2 = []
list3 = []
optimal = None
list_item = []
for i in range(1,4):
	if i == 1:
		for j in range(1, W+1):
			result = knapSack(j, wt[0:i], val[0:i], i)
			list1.append(result)
		for item in list1:
			print(item, end='	')
			optimal = item
		print()
	elif i == 2:
		for j in range(1, W+1):
			result = knapSack(j, wt[0:i], val[0:i], i)
			list2.append(result)
		for item in range(len(list2)):
			if(list1[item] != list2[item]):
				print(list2[item], end='	')
			else: print(' ', end='	')
			if (optimal < list2[item]):  # Optimal value
				optimal = list2[item]
				temp = optimal
				list_item = bestPlan(val,temp,2, 0, 0, 0)
		print()
	else:
		for j in range(1, W+1):
			result = knapSack(j, wt[0:i], val[0:i], i)
			list3.append(result)
		for item in range(len(list3)):
			if(list2[item] != list3[item]):
				print(list3[item], end='	')
			else:
				print(' ', end='	')
			if(optimal < list3[item]):  # Optimal value
				optimal = list3[item]
				temp = optimal
				list_item = bestPlan(val,temp,3, 0, 0, 0)
		print()
print('Optimal value:', optimal)
print('item1:', list_item[0])
print('item2:', list_item[1])
print('item3:', list_item[2])