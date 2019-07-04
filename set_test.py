from set import TheGodSet
import unittest


class TestSet(unittest.TestCase):
    def test_init(self):
        st = TheGodSet(4)
        assert len(st.set.buckets) == 4
        assert st.set.length() == 0
        assert st.set.size == 0

    def test_add_and_contains(self):
        st = TheGodSet(8)
        st.add('I', 1)
        st.add('V', 5)
        st.add('X', 10)
        assert st.contains('I') is True
        assert st.contains('V') is True
        assert st.contains('X') is True
        assert st.contains('A') is False

    def test_remove(self):
        st = TheGodSet(8)
        st.add('I', 1)
        st.add('V', 5)
        st.add('X', 10)
        assert st.length() == 3
        assert st.size == 3
        st.remove('I')
        st.remove('X')
        assert st.length() == 1
        assert st.size == 1

    def test_is_subset(self):
        set1 = TheGodSet(8)
        set2 = TheGodSet(8)
        set3 = TheGodSet(8)
        set4 = TheGodSet(8)
        set1.add('I', 1)
        set1.add('V', 5)
        set1.add('X', 10)
        set2.add('I', 1)
        set2.add('V', 5)
        set2.add('O', 10)
        set3.add('I', 1)
        set3.add('V', 5)
        set4.add('I', 1)
        set4.add('O', 5)
        assert set2.is_subset(set3) is True
        assert set2.is_subset(set4) is True
        assert set1.is_subset(set3) is True
        assert set1.is_subset(set4) is False

    def test_union(self):
        set1 = TheGodSet(8)
        set2 = TheGodSet(8)
        set1.add('I', 1)
        set1.add('V', 5)
        set1.add('X', 10)
        set1.add('L', 1)
        set1.add('W', 5)
        set2.add('I', 1)
        set2.add('V', 5)
        set2.add('O', 10)
        set2.add('Z', 1)
        set2.add('P', 5)
        union = set2.union(set1)
        assert union.contains('I') is True
        assert union.contains('W') is True
        assert union.contains('P') is True
        assert union.size == 8

    def test_difference(self):
        set1 = TheGodSet(8)
        set2 = TheGodSet(8)
        set1.add('V', 5)
        set1.add('X', 10)
        set1.add('I', 1)
        set1.add('L', 1)
        set1.add('W', 5)
        set2.add('I', 1)
        set2.add('V', 5)
        set2.add('O', 10)
        set2.add('Z', 1)
        set2.add('P', 5)
        different = set2.difference(set1)
        assert different.contains('W') is True
        assert different.contains('O') is True
        assert different.contains('I') is False
        assert different.contains('V') is False
        assert different.size == 6

    def test_intersection(self):
        set1 = TheGodSet(8)
        set2 = TheGodSet(8)
        set1.add('I', 1)
        set1.add('V', 5)
        set1.add('X', 10)
        set1.add('L', 1)
        set1.add('W', 5)
        set2.add('I', 1)
        set2.add('O', 10)
        set2.add('Z', 1)
        set2.add('V', 5)
        set2.add('P', 5)
        intersection = set1.intersection(set2)
        assert intersection.contains('I') is True
        assert intersection.contains('V') is True
        assert intersection.contains('L') is False
        assert intersection.contains('P') is False
        assert intersection.size == 2

if __name__ == '__main__':
    unittest.main()
