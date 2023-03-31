from Student import Student
class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap*[None]
        self.n = cap
    def hashFunction(self, mykey):
        if self.hashtable[mykey%self.n] != None:
            self.hashtable[mykey%self.n]   
            return True  
        else:
            return False

    def rehashFunction(self, hashkey):
        num = 0
        while self.hashFunction(hashkey) == False:
            hashkey += 1
            num += 1
            if num == self.n:
                return False
        return True

    def insertData(self, student_obj):
        id = student_obj.getId()
        canInsert = True
        if self.hashFunction(id) == False:
            if self.rehashFunction(id) == False:
                canInsert = False
        if canInsert:
            print("Insert", student_obj.getId(), "at index")
        else:
            print("Can't not insert", student_obj.getId())
    def searchData(self, key):
        # ดักไว้ว่ารันครบเท่ากับก็คือตันแล้ว
        check = key%self.n #
        have = False
        fir = check#
        while self.hashFunction(check):
            if self.hashtable[check].getId() == key:
                have = True
                break
            check += 1#
            if check == self.n:
                check = 0
            if fir == check:
                break
        if have:
            print("Found", key, "at index", check)
            return self.hashtable[check]
        else:
            print(key, "does not exist.")
