# code to display and insert data ina hash table using class hashTable
class hashTable:
    def __init__(self, size):
        self.size= size 
        self.table= [[] for _ in range(size)]
    def hash_function(self, key):
        return key % self.size  
    def insert(self, key):
        index= self.hash_function(key)
        self.table[index].append(key)
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
size = int(input("Enter the size of the hash table: "))
ht= hashTable(size)
n= int(input("Enter the number of elements to insert: "))
for i in range(n):
    key= int(input("Enter the key to insert: "))
    ht.insert(key)
ht.display()