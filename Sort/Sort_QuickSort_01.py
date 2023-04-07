from Color_String import bcolors

def partition(array, low, up, k):
    pivot = array[low]   # Lấy pivot là phần tử đầu tiên của dãy
    print('pivot =', pivot)
    i, j = low, up
    while (i < j):
        while (array[i] <= pivot and i < up):
            i = i + 1
        #
        while (array[j] > pivot):
            j = j - 1
        #
        if (i < j):
            print('a[i] a[j] =', array[i], array[j])
            array[i], array[j] = array[j], array[i]  # SWAP
    print('a[low] a[j] =', array[low], array[j])
    if(array[low] is array[j]):
        print('Pivot Duplicated!!!')
    else:
        array[low], array[j] = array[j], array[low]
    pivotIndex = j
    if(pivotIndex == k):
        print('=============>> Phan tu thu' , k+1 ,'la: ', array[pivotIndex], bcolors.OKGREEN)
        return pivotIndex
    return pivotIndex

def quickSort(array, Low, Up, k):
    print('-------------------',array)
    if (Low >= Up):
        print('Next Pivot')
        return
    pivot = partition(array, Low, Up, k)
    quickSort(array, Low, pivot - 1, k)
    quickSort(array, pivot + 1, Up, k)

array = [5, 3, 4, 6, 1, -9, 23, -6, 10, 12]
# array = [7, 3, 5, 9, 11, 8, 6, 15, 10, 12, 14]
n = len(array)
k = int(input('Nhap phan tu thu k: ')) - 1
quickSort(array, 0, n - 1, k)
print('After sort:')
print(array)
