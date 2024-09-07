# Double-base palindromes
Consider the binary representation. Since the number is a palindrome, the lowest and highest bits must be the same. And since the number cannot have leading zeroes, it follows that the lowest and highest bits must be 1.

$2^{20}$ = 1048576, which is larger than one million. So the binary representation must have no more than 20 bits.

Now, we can construct all palindromes in binary, up to 20 bits and with lowest and highest bits both set to 1, then check if it is a palindrome in decimal as well.
