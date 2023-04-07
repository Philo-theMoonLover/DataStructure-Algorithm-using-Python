# Recursive solution for Rod cutting problem

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, index, n):
    # base case
    if index == 0:
        return n * price[0]

    # At any index we have 2 options either cut the rod of this length or not cut it
    notCut = cutRod(price, index - 1, n)
    cut = float("-inf")
    rod_length = index + 1

    if (rod_length <= n):
        cut = price[index] + cutRod(price, index, n - rod_length)
    print('Compare',str(notCut).rjust(2), 'and', str(cut).rjust(4), ':',max(notCut,cut))
    return max(notCut, cut)

# Driver program to test above functions
arr = [2, 5, 9, 6]
size = len(arr)

# Best for n=5
print("Maximum Obtainable Value is ", cutRod(arr, size-1, 5))
