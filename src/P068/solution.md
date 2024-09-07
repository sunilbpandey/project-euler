# Magic 5-gon ring
This problem can actually be solved manually without any programming.

Since we are looking for a 16-digit string, the number 10 must be in one of the external nodes.

Now, to generate the string, we start with the numerically lowest external node. Since there are five external nodes, the string can never start with 7, 8 or 9, because those nodes will never be numerically lowest.

Since we are looking for the maximum string, it must start with 6 and the external nodes must be 6, 7, 8, 9 and 10, in some order.

Each internal node appears in two groups of three. The sum of all the groups must be 2 * (sum of all internal nodes) + (sum of all external nodes), i.e. 2 * (1 + 2 + 3 + 4 + 5) + 6 + 7 + 8 + 9 + 10 = 70.

Since there are five groups of three, each group must add up to 14.

For the group containing 6, there are only two possible solutions: (6, 3, 5) and (6, 5, 3). Since we are looking for the maximum string, let's pick (6, 5, 3).

For the group containing 10, again there are only two possible solutions: (10, 1, 3) and (10, 3, 1). But since we picked (6, 5, 3), the only solution for 10 is (10, 3, 1). Also, because of the 3, 10 must be the next external node clockwise from 6.

Continuing like this, we can see that the group containing 9 must be (9, 1, 4) and it must be the next external node clockwise from 10.

The next external node in the clockwise direction must be 8, with the group by (8, 4, 2). And the final group must be (7, 2, 5).

This gives us the answer: 6531031914842725.
