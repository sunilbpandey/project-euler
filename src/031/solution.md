# Coin sums
A simple way of solving this is using recursion. Let's say we were trying to make £4. We could use two £2 coins, or we could use one £1 coin and try to make the remaining £1 using only the other coins, or we could skip £2 coin altogether and try to make £2 using only the other coins.

So, at every step of the recursion, try to take none or as many as possible of the highest denomination coin, then count the number ways the remaining amount can be made using all the coins except this coin.
