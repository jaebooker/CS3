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
        # with self.assertRaises(KeyError):
        #     st.delete('X')  # Key no longer exists
        # with st.assertRaises(KeyError):
        #     ht.delete('A')  # Key does not exist

if __name__ == '__main__':
    unittest.main()
