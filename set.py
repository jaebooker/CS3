from hashtable import HashTable

class TheGodSet(object):
    def __init__(self, num):
        self.size = 0
        self.set = HashTable(num)

    """Length() returns the number of key-value entries by traversing its buckets.
    Best and worst case running time: O(n) because it must traverse all entries in bucket"""
    def length(self):
        return self.set.length()

    """Add() inserts or updates the given key with its associated value.
    Best case running time: O(1) because it is first in hash table, or else shares with no other items
    Worst case running time: O(n) because all items are clustered somehow in just one hash"""
    def add(self, key, item):
        self.set.set(key, item)
        self.size += 1

    """Remove() deletes the given key and its associated value, or raise KeyError.
    Best case running time: O(1) because it is first in hash table, or else shares with no other items
    Worst case running time: O(n) because all items are clustered somehow in just one hash"""
    def remove(self, key):
        self.set.delete(key)
        self.size -= 1

    """Contains() returns True if this hash table contains the given key, or False.
    Best case running time: O(1) because all it needs to know is if it is in the hash table
    Worst case running time: O(1) because it's just a basic check, no iteration needed"""
    def contains(self, key):
        return self.set.contains(key)


    """Intersection() is where two sets collide, seeing where two sets have common interests... er, elements
    Best and worst case running time: O(n) because all elements must be traversed in both sets"""
    def intersection(self, set2):
        pass

    """Union() joins two sets in unholy matromony, till deletion do they part, adding all unique elements
    Best and worst case running time: O(n) because it must traverse all entries in both sets"""
    def union(self, set2):
        pass

    """Is_Subset() checks to see if there might be a small subset growing insight one of the sets,
    with elements shared by the other set
    Best case and worst case running time: O(m) where m is the subset that must be checked"""
    def is_subset(self, set2, subset):
        for i in subset:
            if self.contains(i) == False:
                return False
        return True

    """Difference() is where two sets realize they may have a whole lot of different elements
    Best and worst case running time: O(n) because it must traverse both sets completely"""
    def difference(self, set2):
        pass
