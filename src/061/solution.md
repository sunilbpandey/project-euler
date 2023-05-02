# Cyclical figurate numbers
Given a number in the set, we need to find the next number whose first two digits are same as the last two digits of the given number. To do this easily, we can generate all the figurate numbers and group by them their first two digits.

Also, since the set is cyclic, it doesn't matter which number we start with. So, take each octagonal number, since they are the fewest, and see if we can find a cyclic set of six numbers starting with that number.
