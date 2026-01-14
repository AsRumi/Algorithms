'''
Numbers are represented in binary format. Bitwise operations happen on these representations.

There are a few bitwise operators in Python: & - and, | - or, ^ - xor, ~ - not, << - left shift, >> - right shift

And performs bitwise and. Similar operation from or and xor and not. Not also flips the sign bit.

Left shift shifts all the bits left, filling the right side with zeros.
Example: 5 << 1 -> 101 << 1 -> 1010 therefore 5 after one left shift becomes 10 
Effect of left shifting is multiplying the number with 2

Right shift shifts all the bits to the right, trashing the bits that were shifted.
Example: 5 >> 1 -> 101 >> 1 -> 10 therefore 5 after one right shift becomes 2
Effect of right shifting is dividing the number with 2

Negative numbers are represented in binary with a sign bit. This bit is present to the left of the binary representation.
To find out the negative binary representation of any number, apply the 2's complement to the binary representation of that number.
'''

# Essential Bit Tricks:

# 1. Check if a bit at position i is set, formula: n & (1 << i) != 0
# You are essentially moving a window of one bit over the number and checking its binary bit using the and operator
# Do not try to check if the bit is set or not by comparing the result to 1 instead of 0; like so: n & (1 << i) == 1
print(f"Binary of 5 is 101:")
for i in range(3):
    print(f"Is bit at position {i} in 5 set to 1? {5 & (1 << i) != 0}")
    
# 2. Set a bit at position i to 1, formula: n | (1 << i)
# You are moving a bit by i positions to the left and using the OR operator to set it to 1 even if it is a 0
# Example: Binary 10 (= 2) can be set to binary 1010 (= 10) as such:

n = 2
print(f"{n} was changed to {n | (1 << 3)} by setting its bit.")

# 3. Clearing a bit at position i, formula: n & ~(1 << i)
# You need to move the 1 bit by position i. Once you have the bit at the right position to clear, inverse the entire binary number so you end up with all ones except the position to be cleared. Use and operator to retain the bit at every other position except at position i.
# Example : 1110 can be converted to 1010 by clearing its bit at position 2 (indexing starts from 0 from the left)

n = int('1110', 2)
print(f"{n} was converted to {n & ~(1 << 2)} by clearing its bit at position 2.")

# 4. Toggle bit at position i by using the XOR operation, formula: n ^ (1 << i)

n = int('110101', 2)
print(f"{n} was converted to {n ^ (1 << 4)} by toggling its bit at position 5.")

# You can also check if a number is a power of 2 using the formula: n & n-1 == 0
# A power of 2 has only a single digit as one, and the number before it has all its previous bits 1
# Using and operator on both of these numbers gives you 0. This is only true for powers of 2

# You can also get the rightmost set bit by (n & -n) and clear the rightmost set bit by (n & (n-1))

# Write a function to count the number of set bits in a number:
def count_set_bits(n):
    k = 1
    count = 0
    while True:
        if n & k != 0:
            count += 1
        k = k << 1
        if k > n:
            break
    return count

n = int('101101101', 2)
print(f"Number of set bits in {n} = {count_set_bits(n)}")