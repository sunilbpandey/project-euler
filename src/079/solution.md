# Passcode Derivation
This problem can be solved in multiple ways. In fact, it can be easily solved with just pen and paper! One nice, general way of solving problems like this is using [topological sort](https://en.wikipedia.org/wiki/Topological_sorting).

We know that the characters of the guess will always be in order. So if we see a guess "319", that means "3" must come before "1" and "9" and "1" must come before "9". We can construct a directed graph where each character is a node, and there is an edge from one character to another if the second character comes after the first one. So in case of "319", we will have three edges "3" -> "1", "3" -> "9" and "1" -> "9". Now we can use depth-first search to sort the nodes.
