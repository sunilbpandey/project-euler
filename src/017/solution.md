# Number letter counts
There is no clever math involved here, just a simple set of rules:

- All numbers below 20 have unique names - "one", "two", ... "nineteen"
- For numbers above 19 and below 100, extract the decade, which has a unique name, then use the above rule to name the remainder - e.g. "twenty one", "fifty six" etc.
- For numbers above 99, extract the century, then use the above rules to name the remainder - e.g. "two hundred and thirty nine" etc.

## Alternate approach
Instead of going through each number and writing out its name, we can compute the answer more directly.

The word "one" appears 90 times at the end of the name - "one", "twentyone", "thirtyone", "onehundredandfortyone", and so on. It also appears 100 times at the beginning of the name, for all numbers between 100 and 199. Similarly, words "two" to "nine" also appear 190 times each.

The words "ten" to "nineteen" each appear 10 times - "ten", "onehundredandten", "twohundredandten", and so on.

The words "twenty", "thirty", and so on till "ninety" each appear 100 times - "twenty", "twentyone", "twentytwo", "fourhundredandtwentythree", and so on.

The word "hundred" appears 900 times, in all numbers from 100 to 999.

The word "and" appears 891 times, in all numbers from 100 to 999 except 100, 200, 300 and so on.

And finally, "onethousand" appears once.
