from Student import Student
from ProbHash import ProbHash
s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)

myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

std = myHash.searchData(65070077)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070032)
