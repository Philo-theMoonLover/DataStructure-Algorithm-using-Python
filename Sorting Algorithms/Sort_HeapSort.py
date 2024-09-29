'''
Heap sort
Time complexity: O(n log(n)) for all cases
'''
'''
Heapify: dùng để tạo min-heap hoặc max-heap
'''
# Lấy từng phần tử gốc đặt vào cuối

'''
Lưu ý: heapify chỉ có thể được áp dụng cho một nút nếu các nút con của nó được heapified.
       Vì vậy, heapify phải được thực hiện theo thứ tự từ dưới lên.
'''
def heapify(arr, N, i):
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is smaller than root
    if left < N and arr[left] < arr[smallest]:
        smallest = left
    # See if right child of root exists and is smaller than root
    if right < N and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root, change root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # SWAP
        heapify(arr, N, smallest)

def heapSort(arr, N, k):
    # N=11, i chạy từ 4 đến 0
    # Total non-leaf nodes = N//2-1

    # arr1 = list()
    # for i in arr:
    #     arr1.append(i)
    #     for k in range(len(arr1)//2-1, -1, -1):
    #         heapify(arr1, len((arr1)), k)

    for i in range(N//2-1, -1, -1):  # Build a minheap, step=-1
        heapify(arr, N, i)
    print('Array after build minheap', arr)
    # Rút từng phần tử
    for i in range(N-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # SWAP phần tử đầu vs cuối của mảng
        print('SWAP',arr)
        # if(i == 5):
        #     result = list(reversed(arr[0:N-i]))
        #     print(result)
        if (k == N-i-1):
            print('5th order statistic:', arr[i])

        # Lấy từng node build lại cây với N' = i (phần tử cuối bị xóa)
        heapify(arr, i, 0)
        #print('and',arr1)

array = [11, 7, 5, 10, 8, 12, 3, 2, 6, 13, 4]
print('Initial Array:', array)
k = int(input('Nhap phan tu thu k = ')) - 1
N = len(array)
heapSort(array, N, k)
print('Sorted array:', array)

'''
                    11
                  /    \
                 /      \
                7        5
              /  \      / \
             10   8    12  3
            / \  / \
           2  6  13 4
'''