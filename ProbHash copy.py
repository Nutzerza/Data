from Student import Student
class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap*[None]
        self.n = cap
    def hashFunction(self, mykey):
        return True if self.hashtable[mykey] != None else False
    def rehashFunction(self, hashkey):
        return True if self.hashtable[hashkey] != None else False
    def insertData(self, student_obj):
        canInsert = True
        check = student_obj.getId()%self.n
        fir = check
        if self.hashFunction(check):
            while self.rehashFunction(check):
                check = check+1
                if check == self.n:
                    check = 0
                if fir == check:
                    canInsert = False
                    break
        if canInsert:
            self.hashtable[check] = student_obj
            print("Insert", student_obj.getId(), "at index", check)
        else:
            print("Can't not insert", student_obj.getId())
    def searchData(self, key):
        check = key%self.n
        have = False
        fir = check
        while self.hashFunction(check):
            if self.hashtable[check].getId() == key:
                have = True
                break
            check += 1
            if check == self.n:
                check = 0
            if fir == check:
                break
        if have:
            print("Found", key, "at index", check)
            return self.hashtable[check]
        else:
            print(key, "does not exist.")
