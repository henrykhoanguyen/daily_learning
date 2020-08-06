'''
Problem: 705. Design HashSet
        design a hashset with (add, remove, contains) functionality
Input: key - int; integer to be add into hashset
Output: contains(key) - return boolean value if such key exist in
        hashset.
        add(key), remove(key) - return None.
Explanation:
        We hash each key by mod it to 1000 to get a subkey that is
        gonna be that key's index in an array list. If that index
        is occupied, then searched key exists; else no. Only add
        key if it doesn't exist. Only remove key if it exists.
'''

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        subkey = key % 1000
        if key not in self.hashset[subkey]:
            self.hashset[subkey].append(key)

    def remove(self, key: int) -> None:
        subkey = key % 1000
        if key in self.hashset[subkey]:
            self.hashset[subkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        subkey = key % 1000
        if key in self.hashset[subkey]:
            return True
        return False


hashSet = MyHashSet()
print(hashSet.add(1))
print(hashSet.add(2))
print(hashSet.contains(1))
print(hashSet.contains(3))
print(hashSet.add(2))
print(hashSet.contains(2))
print(hashSet.remove(2))
print(hashSet.contains(2))
