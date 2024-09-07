# Anagramic Squares

Start by grouping all the anagram words together, by sorting the letters in each word. Then collect all the groups that have more than one word. We find that the pair with the longest words is INTRODUCE and REDUCTION, with nine letters each. We can also skip any three-letter anagrams since CARE and RACE are also in the list.

The smallest four-digit square number is $32^2 = 1024$. The largest nine-digit square number is $31622^2 = 999\,950\,884$. So generate squares of all numbers from 32 to 31622, group them together just like the anagram words, and collect groups with more than one number.

Now go through the square groups in descending order of number of digits. For each group, first find compatible anagram groups. To do this, count the number of each digit in the square, and count the number of each letter in the anagram. For two groups two be compatible, the counts of occurrences should match. E.g. 368449 contains one digit, 4, twice and four digits, 3, 6, 8 and 9, once each; the word CENTRE contains one letter, E, twice and four letters, C, N, R and T, once each. Since the counts match, these two groups are compatible.

Finally, take every square number in the group, map it to the first word in the anagram pair, and apply the same letter substitution to all other numbers in the group. If any of the other numbers produces the second word in the pair, we have our answer!
