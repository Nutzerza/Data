
class ProbHash:
    def __init__(self, cap):
        self.hashTable = cap*[None]
        self.n = cap
    def hashFunction(self, mykey):
        return mykey%self.n
    def rehashFunction(self, hashKey):
        return hashKey + 1
    def insertData(self, studentOBJ):
        idStu = studentOBJ.getId()
        hashKey = self.hashFunction(idStu)
        count = 0
        if self.hashTable[hashKey]:
            while self.hashTable[hashKey]:
                hashKey = self.rehashFunction(hashKey)
                if count == self.n:
                    print(idStu, "can't insert.")
                    return
            self.hashTable[hashKey] = studentOBJ
        else:
            self.hashTable[hashKey] = studentOBJ
        print("Insert", idStu, "at index", hashKey)
    def searchData(self, key):
        hashKey = self.hashFunction(key)
        check = False
        count = 0
        if self.hashTable[hashKey] == None:
            check = True
        elif self.hashTable[hashKey].getId() != key:
            while self.hashTable[hashKey].getId() != key:
                hashKey = self.rehashFunction(hashKey)
                if self.hashTable[hashKey] == None and count == self.n:
                    check = True
                    break
                count += 1
        if check:
            print(key, "does not exist.")
            return None
        else:
            std = self.hashTable[hashKey]
            print("Found", key, "at index", hashKey)
            return std
