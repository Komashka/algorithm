class MaxHeap:
    def __init__(self):
        self.arr = []

    def maxheapify(self, x):
        if len(self.arr) <= 1:
            return True
        largest = x
        l = 2 * x + 1
        r = 2 * x + 2
        if l < len(self.arr) and self.arr[l] > self.arr[x]:
            largest = l
        if r < len(self.arr) and self.arr[r] > self.arr[x] and self.arr[r] > self.arr[l]:
            largest = r
        if largest != x:
            item = self.arr[x]
            self.arr[x], self.arr[largest] = self.arr[largest], item
            self.maxheapify(largest)
        else:
            return self.arr

    def buildmaxheap(self):
        heap_size = len(self.arr)
        for i in range(heap_size // 2, - 1, -1):
            self.maxheapify(i)

    def insert(self, a):
        self.arr.append(a)
        self.buildmaxheap()

    def delete(self, a):
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        self.arr.pop(len(self.arr) - 1)
        self.maxheapify(0)

    def max(self):
        return self.arr[0]

    def my_max_arr(self):
        return self.arr