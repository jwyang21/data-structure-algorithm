# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
import random
class RandomizedSet:

    def __init__(self):
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.l:
            self.l.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.l:
            self.l.remove(val)
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.sample(self.l, 1)[0]
