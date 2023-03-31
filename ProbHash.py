from Student import Student
class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap*[None]
        self.n = cap
    def hashFunction(self, mykey):
        pos = mykey%self.n
        if self.hashtable[pos] == None:
            return pos
        else:
            return self.hashtable[pos]
    def rehashFunction(self, hashkey):
        num = 0
        while type(self.hashFunction(hashkey)) != int:
            hashkey += 1
            num += 1
            if num == self.n:
                return False
        return hashkey%self.n
    def insertData(self, student_obj):
        id = student_obj.getId()
        pos = self.rehashFunction(id)
        if pos!=False:
            self.hashtable[pos] = student_obj
            print("Insert", student_obj.getId(), "at index", pos)
        else:
            print("Can't not insert", student_obj.getId())
    def searchData(self, key):
        pos = self.rehashFunction(key)
        return self.hashtable[pos]
