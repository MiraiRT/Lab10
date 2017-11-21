class heap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def insert(self, data):
        print('Insert :', data)
        if self.heapList == [0]:
            self.size = self.size + 1
            self.heapList.append(data)
        else:
            self.size = self.size + 1
            self.heapList.append(data)
            i = self.size
            while i // 2 > 0:
                if self.heapList[i] < self.heapList[i // 2]:
                    tmp = self.heapList[i // 2]
                    self.heapList[i // 2] = self.heapList[i]
                    self.heapList[i] = tmp
                i = i // 2

    def order(self):
        print('Heap :', end=' ')
        for i in range(1, self.size + 1):
            print(self.heapList[i], end=' ')
        print()

    def printSideWay(self, index, lvl):
        if (2 * int(index)) + 1 < self.size:
            heap.printSideWay(self, 2 * int(index) + 1, lvl + 1)
        print(lvl * '   ', self.heapList[index])
        if (2 * int(index)) < self.size:
            heap.printSideWay(self, 2 * int(index), lvl + 1)


l = [5, 7, 4, 1, 3, 6, 9, 2, 8, 0]
##l = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
h = heap()
for ele in l:
    h.insert(ele)
    h.order()
    h.printSideWay(1, 0)
