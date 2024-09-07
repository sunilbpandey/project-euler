# Digit Factorial Chains
We do need to calculate the chains of all the numbers, but we can do one optimization.

Consider the following chain:

    27 → 5042 → 147 → 5065 → 961 → 363601 → 1454 → 169 (→ 363601)

Clearly, chain length of 27 is 8. But we can also see that chain length of 5042 is 7, that of 147 is 6, and so on. This way we can avoid calculating the chains for these numbers again.
