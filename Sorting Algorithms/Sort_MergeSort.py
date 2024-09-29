'''
Merge sort
Time complexity: O(n log(n)) in all cases
'''
def merge(arr, left, mid, right):
    x = mid - left + 1
    y = right - mid
    # temp lists
    L = [0] * x
    R = [0] * y
    # copy elements to temp lists
    for i in range(0, x):
        L[i] = arr[left + i]
    for j in range(0, y):
        R[j] = arr[mid + 1 + j]
    print('L =', L)
    print('R =', R)
    # merge 2 temp lists vào arr[left..right]
    i, j, k = 0, 0, left
    while i < x and j < y:
        if L[i] <= R[j]:  # so sánh 2 phần tử đang được trỏ đến của L và R
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # copy phần tử còn lại của L[] hoặc R[] nếu còn
    while i < x:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < y:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left = None, right = None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

array = [2, 23, 14, 9, 1, -9, 23, -6, 20, 12]
print('Initial Array:', array)
# k = int(input('Nhap phan tu thu k = ')) - 1
mergeSort(array, None, None)
print('Sorted array:', array)