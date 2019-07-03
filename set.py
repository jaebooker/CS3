from hashtable import HashTable

class TheGodSet(object):
    def __init__(self, num):
        self.size = 0
        self.set = HashTable(num)

    def length(self):
        return self.set.length()

    def add(self, key, item):
        self.set.set(key, item)
        self.size += 1

    def remove(self, key):
        self.set.delete(key)
        self.size -= 1

    def contains(self, key):
        return self.set.contains(key)
