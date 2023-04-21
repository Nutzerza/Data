class Sorting:
    def __init__(self):
        self.point = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        self.flow = {
            "♣": 2,
            "♦": 3,
            "♥": 4,
            "♠": 5
        }
    def insertionSort(self, inList, lst):
        current = 1
        comparison = 0
        while current <= lst:
            hold = current
            walker = current-1
            while walker >= 0:
                if self.point[inList[walker][:-1]] < self.point[inList[current][:-1]]:
                    comparison += 1
                    break
                if self.point[inList[walker][:-1]] == self.point[inList[current][:-1]]:
                    if self.flow[inList[walker][-1]] < self.flow[inList[current][-1]]:
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
                # print(smallest)
                if self.point[inList[walker][:-1]] < self.point[inList[smallest][:-1]]:
                    # print("kuy")
                    smallest = walker
                if self.point[inList[walker][:-1]] == self.point[inList[smallest][:-1]]:
                    # print("walk", self.flow[inList[walker][-1]], "cur", self.flow[inList[smallest][-1]])
                    if self.flow[inList[walker][-1]] < self.flow[inList[smallest][-1]]:
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
                if inList[walker][:-1] < inList[walker-1][:-1]:
                    sorTed = False
                    inList[walker], inList[walker-1] = inList[walker-1], inList[walker]
                walker -= 1
                comparison += 1
            print(inList)
            current += 1
        print(comparison)

sorting = Sorting()
# sorting.insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
# sorting.selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)

# sorting.insertionSort(['J♣', 'A♣', 'K♥', 'Q♦', '10♠'], 4)
