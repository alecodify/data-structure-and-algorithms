"""
The Hash table data structure stores elements in key-value pairs where
Key- unique any that is used for indexing the values
Value - data that are associated with keys.
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None 

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False


hash_table = HashTable(10)
hash_table.insert("name", "Ali")
hash_table.insert("age", 22)

print(hash_table.search("name"))  # Output: Ali
print(hash_table.search("age"))   # Output: 22

hash_table.delete("age")
print(hash_table.search("age"))   # Output: None
