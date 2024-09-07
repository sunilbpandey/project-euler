# Convergents of e
Let $t_1, t_2, t_3, ... $ be the convergents of the continued fractions for $e$.

$t_1 = 2$

$t_2 = 2 + \frac{1}{1} = 3$

$t_3 = 2 + \frac{1}{1 + \frac{1}{2}} = 2 + \frac{2}{3} = \frac{8}{3}$

$t_4 = 2 + \frac{1}{1 + \frac{1}{2 + \frac{1}{1}}} = 2 + \frac{1}{1 + \frac{1}{3}} = 2 + \frac{3}{4} = \frac{11}{4}$

and so on.

To find the kth term, start with $\frac{3}{2k}$ if k is divisible by 3, or 1 if k is not divisible by 3. Then repeat the following steps k - 2 times:

1. If this is the $i^{th}$ iteration (where i starts at 1) and k - i is divisible by 3, then add $\frac{2(k - i)}{3}$, otherwise add 1
1. Take the reciprocal of the fraction

Finally, add 2 and simplify the fraction.

## Using the formula for numerator
Consider the continued fraction $[a_1; a_2, a_3, \dots]$

The first convergent is $a_1$.

The second convergent is $a_1 + \frac{1}{a_2} = \frac{a_1a_2 + 1}{a_2}$

The third convergent is $a_1 + \frac{1}{a_2 + \frac{1}{a_3}} = \frac{a_1a_2a_3 + a_1 + a_3}{a_2a_3 + 1} = \frac{a_3(a_1a_2 + 1) + a_1}{a_2a_3 + 1}$

The fourth convergent is $a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \frac{1}{a_4}}} = \frac{a_1a_2a_3a_4 + a_1a_2 + a_1a_4 + a_3a_4 + 1}{a_2a_3a_4 + a_2 + a_4} = \frac{a_4(a_1a_2a_3 + a_1 + a_3) + a_1a_2 + 1}{a_2a_3a_4 + a_2 + a_4}$

The numerator of the ith convergent, where i > 2, can be found using this simple formula:

$h_i = a_i \times h_{i - 1} + h_{i - 2}$

Although not needed for this problem, the denominator can be found using a similar formula:

$k_i = a_i \times k_{i - 1} + k_{i - 2}$

In case of $e$, the continued fraction representation is:

$e = [2; 1, 2, 1, 1, 4, 1, 1, 6, \dots, 1, 2k, 1, \dots]$

We can see that, if k is divisible by 3, $a_k = \frac{2k}{3}$, otherwise $a_k = 1$.
