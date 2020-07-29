import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not self.dic.get(val):
            self.dic[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.dic.get(val):
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice([key for key in self.dic.keys()])
        # return random.choice(self.dic.items())

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.remove(1)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.getRandom()