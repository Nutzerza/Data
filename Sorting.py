class Sorting:
    def insertionSort(self, inList, lst):
        current = 1
        comparison = 0
        while current <= lst:
            hold = current
            walker = current-1
            while walker >= 0:
                if inList[walker] < inList[current]:
                    comparison += 1
                    break
                walker -= 1
                comparison += 1
            inList.insert(walker+1, inList.pop(hold))
            print(inList)
            current += 1
        print(comparison)

    def selectionSort(self, inList, lst):
        current = 0
        comparison = 0
        while current < lst:
            smallest = current
            walker = current + 1
            while walker <= lst:
                if inList[smallest] > inList[walker]:
                    smallest = walker
                walker += 1
                comparison += 1
            inList[current], inList[smallest] = inList[smallest], inList[current]
            print(inList)
            current += 1
        print(comparison)

    def bubbleSort(self, inList, lst):
        current = 0
        comparison = 0
        sorTed = False
        while current<=lst and sorTed == False:
            walker = lst
            sorTed = True
            while walker > current:
                if inList[walker] < inList[walker-1]:
                    sorTed = False
                    inList[walker], inList[walker-1] = inList[walker-1], inList[walker]
                walker -= 1
                comparison += 1
            print(inList)
            current += 1
        print(comparison)

sorting = Sorting()
# sorting.insertionSort([23, 78, 45, 8, 32, 56], 5)
# sorting.insertionSort([2, 1, 3, 4, 5, 6], 5)
# sorting.insertionSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)

# sorting.selectionSort([23, 78, 45, 8, 32, 56], 5)
# sorting.selectionSort([2, 1, 3, 4, 5, 6], 5)
# sorting.selectionSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)

# sorting.bubbleSort([23, 78, 45, 8, 32, 56], 5)
# sorting.bubbleSort([2, 1, 3, 4, 5, 6], 5)
sorting.bubbleSort([503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 765, 703], 12)

