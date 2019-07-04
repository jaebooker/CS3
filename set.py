from hashtable import HashTable

class TheGodSet(object):
    def __init__(self, num):
        self.set = HashTable(num)
        self.size = self.length()

    """Length() returns the number of key-value entries by traversing its buckets.
    Best and worst case running time: O(n) because it must traverse all entries in bucket"""
    def length(self):
        return self.set.length()

    """Add() inserts or updates the given key with its associated value.
    Best case running time: O(1) because it is first in hash table, or else shares with no other items
    Worst case running time: O(n) because all items are clustered somehow in just one hash"""
    def add(self, key, item):
        if self.contains(key) == False:
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
    For the sake of simplicity, we're assuming each unique key will have the same value,
    even if the key is in both sets. This assumption will also be the case in all functions below
    Best and worst case running time: O(n) because all elements must be traversed in both sets"""
    def intersection(self, set2):
        if self.size < set2.size: #Checking which set is smaller, since worse case could only be size of smaller set
            new_size = self.size
        else:
            new_size = set2.size
        common_set = TheGodSet(new_size * 2) #Preparing for all common entries, doubling smaller set
        for i in set2.set.keys():
            if self.contains(i) == True:
                v = self.set.get(i)
                common_set.add(i,v)
        return common_set

    """Union() joins two sets in unholy matromony, till deletion do they part, adding all unique elements
    Best and worst case running time: O(n) because it must traverse all entries in both sets"""
    def union(self, set2):
        union_set = TheGodSet((self.size + set2.size)*2) #Prepares for union having no duplicates
        for i in self.set.keys():
            v = self.set.get(i)
            union_set.add(i,v)
        for z in set2.set.keys():
            v = set2.set.get(z)
            union_set.add(z,v)
        return union_set

    """Is_Subset() checks to see if there might be a small subset growing insight one of the sets,
    with elements shared by the other set
    Best case and worst case running time: O(m) where m is the subset that must be checked"""
    def is_subset(self, subset):
        for i in subset.set.keys():
            if self.contains(i) == False:
                return False
        return True

    """Difference() is where two sets realize they may have a whole lot of different elements
    Best and worst case running time: O(n) because it must traverse both sets completely"""
    def difference(self, set2):
        different_set = TheGodSet((self.size + set2.size)*2) #Preparing for both sets being totally different
        for i in self.set.keys():
            if set2.contains(i) == False:
                v = self.set.get(i)
                different_set.add(i,v)
        for z in set2.set.keys():
            if self.contains(z) == False:
                v = set2.set.get(z)
                different_set.add(z,v)
        return different_set
