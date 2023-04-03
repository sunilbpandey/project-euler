# Pentagon numbers
Given,

$$
P_j + P_k = P_{sum}
$$

and

$$
P_j - P_k = P_{diff}
$$

assuming $P_j \ge P_k$ without loss of generality.

Rearranging the terms, we get,

$$
P_j = P_{sum} - P_k
$$

and,

$$
P_{diff} = P_{sum} - 2P_k
$$

So, as we generate pentagonal numbers, test every new number against all the previously generated ones until we find a suitable pair.

While the current approach produces the correct answer, I cannot prove that the answer is correct. It stops at the first instance it finds, but how can we be sure that no larger numbers will produce a smaller difference? Ideally, we must keep generating the pentagonal numbers until the difference between successive numbers is larger than the answer we have already found, but doing this takes a long time. It may be possible to implement an efficient and provably correct solution using the method described [here](https://projecteuler.net/thread=44;page=4#22003).
