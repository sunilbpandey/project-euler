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
