# Arithmetic Expressions

We need to generate all sets of four distinct digits, and then consider all 24 permutations of these digits. After this, we need to insert the operators. Since there are four digits, there can be at most three operators.

We don't have to worry about operator precedence because we can force precedence using parantheses. Let's assume that the default precedence is left-to-right. So the following groupings are equivalent:

$$
\begin{align*}
a . b . c . d\\
(a . b) . c . d\\
(a . b . c) . d\\
((a . b) . c) . d
\end{align*}
$$

where "$.$" is any one of the three operators.

In fact, there are only five distinct groupings:

$$
\begin{align*}
((a . b) . c) . d\\
(a . (b . c)) . d\\
(a . b) . (c . d)\\
a . ((b . c) . d)\\
a . (b . (c . d))
\end{align*}
$$

So, we generate all sets of four distinct digits, generate all 24 permutations of these digits, apply all 64 possible combination of operators, and finally apply the 5 groupings. Then evaluate each expression and consider the ones that return positive integers.

One further optimization is to use postfix notation instead of infix to represent these expressions. This makes the code a lot simpler.

Finally, note that the largest number that can be generated this way is $6 \times 7 \times 8 \times 9 = 3024$.
