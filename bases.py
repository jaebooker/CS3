#!python
import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
alpha_numbers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_numbers_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rune_numers = ['!','@','#','$','%','^','&','*','(',')','~','``','_','-','+','=','[','{',']','}','|',';',':','"',"'",'<',',','>','.','?','/']

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    """Break string into runes
    Loop through runes
    If the index is zero, just add the given rune to the result
    Otherwise, multiply each non-zero by the base to the power of the index,
    then multiply that result times by given rune
    if base is greater than ten, add ten to its alpha-numeric code (B would equal 2 + 10, C equals 3 + 10, etc.)
    add the output of this to the given result
    """
    result = 0
    # for i, c in enumerate(digits[::-1]):
    #     string = False
    #     for ii,cc in enumerate(alpha_numbers):
    #         if c == cc:
    #             if i == 0:
    #                 result += ii+10
    #             else:
    #                 result += (base ** i)*(ii+10)
    #             string = True
    #             break
    #     if string != True:
    #         if i == 0:
    #             result += int(c)
    #         else:
    #             result += (base ** i)*int(c)
    """Above would have been for custom version of string.printable. But couldn't fix case for decoding base10 into base10"""
    for i, c in enumerate(digits[::-1]):
        result +=  (base ** i) * string.printable.index(c)
    return result
    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    result = []
    num = number
    while num != 0:
        result.append(num % base)
        num = num // base
    reverse_result = ""
    for i in result[::-1]:
        reverse_result += string.printable[i]
    return reverse_result
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    """Use Base 10 as a sort of "middle man"
    Convert the number to base 10, then convert it to second base
    """
    base10_num = decode(digits, base1)
    return encode(base10_num, base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(decode("ADAA", 16))
    # print(decode("00101010", 2))
    # print(decode("010010", 8))
    print(encode(9, 2))
    print(convert("1001", 2, 2))
    print(encode(11, 16))
    #main()
