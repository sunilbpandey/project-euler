# Prime digit replacements
We can solve this by generating prime numbers, then checking if we can replace certain digits to generate other prime numbers.

If the last digit is one of the digits being replaced, it will generate at least 6 numbers that are not prime. So, the last digit must not be replaced.

Let's say we are replacing one digit. Let the sum of the remaining digits be,

$$
S = 3m + k
$$

where $m \ge 0$ and $0 \le k \le 2$.

So for at least three replacements, the resulting number will be divisible by 3. This means we can never get an eight prime value family.

The same goes if we replace two digits, and in fact any number of digits that is not divisible by 3.

Now, if we replace three digits, clearly the sum of those three digits is divisible by 3. Since we started with a prime number, the sum of remaining digits must not be divisible by 3. This means no matter which digit we replace with, the resulting number will not be divisible by 3.

This means the number of digits being replaced must be divisible by 3.

Let's assume, for simplicity, that we can find a solution by replacing three digits.

This means we should start by looking for prime numbers that have at least three repeated digits.
