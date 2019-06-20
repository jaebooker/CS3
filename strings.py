#!python
"""STARTER CODE FROM NEPTUNIUS"""
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    """Best case: O(1)
    Worst case: O(n^2)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == "":
        return True #It seems this should throw an error, but the tests get made when I don't implement this, so... here it is
    #Implements contains here (iteratively and/or recursively)
    counter = 0
    new_counter = 0
    pattern_checker = 0
    while counter < len(text):
        if text[counter] == pattern[0]:
            pattern_checker = 1
            new_counter = counter + 1
            while (pattern_checker < len(pattern)) and (new_counter < len(text)):
                if text[new_counter] == pattern[pattern_checker]:
                    pattern_checker += 1
                    new_counter += 1
                else:
                    break
            if pattern_checker == len(pattern):
                return True
        counter += 1
    return False
def reusable_contains(text, pattern):
    check = find_index(text, pattern)
    if check != []:
        return True
    return False
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    """Best case: O(1)
    Worst case: O(n^2)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == "": #This doesn't make sense to me. But the tests are under the impression that nothing is a pattern
        return 0
    #Implements find_index here (iteratively and/or recursively)
    counter = 0
    new_index = 0
    new_counter = 0
    pattern_checker = 0
    while counter < len(text):
        if text[counter] == pattern[0]:
            pattern_checker = 1
            new_index = counter
            new_counter = counter + 1
            while (pattern_checker < len(pattern)) and (new_counter < len(text)):
                if text[new_counter] == pattern[pattern_checker]:
                    pattern_checker += 1
                    new_counter += 1
                else:
                    break
            if pattern_checker == len(pattern):
                return new_index
        counter += 1
    return None
def reusable_find_index(text, pattern):
    index = find_all_indexes(text, pattern)
    if index != []:
        return index[0]
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    """Best case: O(1)
    Worst case: O(n^2)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    """Alright, I'm gonna try to humor this. The tests believe that nothing is a pattern that should be humored at every index
    So, bare with me, the code below will add each index of the string, to return the pattern of...
    (sigh) nothing... it returns the pattern of nothing"""
    if pattern == "":
        counter = 0
        index_array = []
        while counter < len(text):
            index_array.append(counter)
            counter += 1
        return index_array
    """Returning to sanity. All code below makes sense from now on, I promise"""
    counter = 0
    new_index = 0
    new_counter = 0
    pattern_checker = 0
    index_array = []
    #Implements find_all_indexes here (iteratively and/or recursively)
    while counter < len(text):
        if text[counter] == pattern[0]:
            pattern_checker = 1
            new_index = counter
            new_counter = counter + 1
            while (pattern_checker < len(pattern)) and (new_counter < len(text)):
                if text[new_counter] == pattern[pattern_checker]:
                    pattern_checker += 1
                    new_counter += 1
                else:
                    break
            if pattern_checker == len(pattern):
                index_array.append(new_index)
        counter += 1
    return index_array
# def find_all_indexes(text, pattern):
#     counter = 0
#     index_array = []
#     while counter < len(text):
#         new_text = text[counter:len(text)-1]
#         print(new_text)
#         temp = find_all_indexes(new_text, pattern)
#         if temp != []:
#             index_array.append(temp)
#         counter += 1
#     return index_array

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    print(contains("abxkcdf", "xkcd"))
    print(find_index("xxxab", "abc"))
    print(find_all_indexes("abcdfxkcd", "cd"))
    print(contains("bananas", "nas"))
    print(find_all_indexes('abcabcab', 'abc'))
