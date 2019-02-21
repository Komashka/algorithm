class MinHeap:
    def __init__(self):
        self.arr = []

    def minheapify(self, x):
        if len(self.arr) <= 1:
            return True
        smallest = x
        l = 2 * x + 1
        r = 2 * x + 2
        if l < len(self.arr) and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < len(self.arr) and self.arr[r] < self.arr[smallest] and self.arr[r] < self.arr[l] and self.arr[r] < \
                self.arr[x]:
            smallest = r
        if smallest != x:
            item = self.arr[x]
            self.arr[x], self.arr[smallest] = self.arr[smallest], item
            self.minheapify(smallest)
        else:
            return self.arr

    def buildminheap(self):
        heap_size = len(self.arr)
        for i in range(heap_size // 2, - 1, -1):
            self.minheapify(i)

    def insert(self, a):
        self.arr.append(a)
        self.buildminheap()

    def delete(self, a):
        item = self.arr[0]
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        self.arr.pop(len(self.arr) - 1)
        self.minheapify(0)

    def min(self):
        return self.arr[0]

    def my_min_arr(self):
        return self.arr