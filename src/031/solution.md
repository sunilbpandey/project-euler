# Coin sums
A simple way of solving this is using recursion. Let's say we were trying to make £4. We could use two £2 coins, or we could use one £1 coin and try to make the remaining £1 using only the other coins, or we could skip £2 coin altogether and try to make £4 using only the other coins.

So, at every step of the recursion, try to take none or as many as possible of the highest denomination coin, then count the number ways the remaining amount can be made using all the coins except this coin.

We can also reformulate the recursion. To make £4, we can pick one £2 coin and try to make the remaining £2 with all the coins, or we can skip £2 coins and try to make £4 using only the other coins.

While both the recursion-based methods work quite well in this case, we can avoid recursion by using the same logic as the second method, but doing the calculation in reverse.

Let's say we had only 1p coins available. It's easy to see that we can make any amount in exactly one way each.

Now add 2p coins to the mix. Obviously, it won't make any difference to amounts less than 2p. To make 2p,

1. Subtract the highest denomination coin, and count the number of ways to make the remainder, i.e. 0, using all the coins. Trivially, this is one.
1. Add the number of ways to make the original amount, i.e. 2p, using all the coins except 2p. We have already calculated this!

To make 4p, follow the same steps:

1. Subtract the highest denomination coin, and count the number of ways to make the remainder, i.e. 2p, using all the coins. We just calculated this above.
1. Add the number of ways to make the original amount, i.e. 4p, using all the coins except 2p. We have already calculated this.

Proceeding in this manner, we can easily count the number of ways to make £2 using all the coins, without using recursion.
