import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of the left child for the node currently at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Kiểm tra node có p lá
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # SWAP 2 node
    def swap(self, pos1, pos2):
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]

    # heapify the node at pos
    def minHeapify(self, pos):
        # Nếu node k phải lá và lớn hơn bất kì con của nó
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Nếu pos.left < pos.right thì SWAP pos và pos.left
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:  # Ngược lại
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        # Nếu node hiện tại nhỏ hơn node cha
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def printHeap(self):
        # for item in self.Heap[1:self.size+1]:
        #     print(item, end=' ')
        print(self.Heap[1:self.size+1])

    # Function to build the min heap using the minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum element from the heap
    def remove(self, k):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        if self.size == self.maxsize - (k - 1):
            print(str(k-1)+'-th order statistic:', popped)
        if self.size == self.maxsize - k:
            self.printHeap()
            print(str(k)+'-th order statistic:', popped)

if __name__ == "__main__":
    k = int(input('k = '))
    array = [11, 7, 5, 10, 8, 12, 3, 2, 6, 13, 4]
    print(array)
    minHeap = MinHeap(len(array))
    for i in array:
        minHeap.insert(i)

    # minHeap.printHeap()
    for i in range(1,k+1):  # 1 to k
        minHeap.remove(k)

