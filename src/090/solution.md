# Cube Digit Pairs

This can be easily solved by brute force. We can choose 6 digits out of 10 in ${10\choose6} = 210$ ways.

The two cubes together need to make eight digits: 0, 1, 2, 3, 4, 5, 6 and 8. So, they cannot be identical.

This means, from the 210 possible arrangements of digits, we can choose the two cubes in ${210 \choose 2} = 21945$ ways. Now we just have to test each of these pairs and count the ones where every square can be displayed.
