import random

random.seed(5)

def partition(array, low, up):
    pivot = array[low]   # Lấy pivot là phần tử đầu tiên của dãy
    print('pivot =', pivot)
    i, j = low, up
    while i < j:
        while array[i] <= pivot and i < up:
            i = i + 1
        #
        while array[j] > pivot:
            j = j - 1
        #
        if i < j:
            print('a[i] a[j] =', array[i], array[j])
            array[i], array[j] = array[j], array[i]  # SWAP
    print('a[low] a[j] =', array[low], array[j])
    if array[low] is array[j]:
        print('Pivot Duplicated!!!')
    else:
        array[low], array[j] = array[j], array[low]
    pivotIndex = j
    return pivotIndex

def quickSort(array, Low, Up):
    print('-------------------',array)
    if (Low >= Up):
        print('Next Pivot')
        return
    pivot = partition(array, Low, Up)
    quickSort(array, Low, pivot - 1)
    quickSort(array, pivot + 1, Up)

array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print('Array:', array)
quickSort(array, 0, len(array) - 1)
print('After sort:', array)
