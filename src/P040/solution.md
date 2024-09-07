# Champernowne's constant
A brute force approach is to simply construct the number up to the relevant length and then select the appropriate digits. Since we are not doing any arithmetic operations, the number can be stored as a string. This method works, but is very slow and storing the entire number in memory is inefficient and unnecessary.

One optimization is to avoid tracking the entire number. Just keep track of the total length so far, and the current number. As soon as the total length goes past the index we are looking for, we know that the digit we are looking for must be in the current number.

Say we are looking for the 100th digit. We go through the numbers, keep track of the total length, until eventually we get to the number 54, at which point the total length is 99. When we go to the next number, 55, we realize that the total length will now exceed 100. So we are looking for a digit in the number 55. The difference between the index, i.e. 100, and the previous total length, i.e. 99, will tell us which digit in the number we are looking for.

But there is an even better and faster way to calculate the digits more directly.

There are 9 one-digit numbers, so $d_1$ to $d_9$ will be 1 to 9. These are followed by 90 two-digit numbers, which make up 180 digits. This is followed by 900 three-digit numbers, which make up 2700 digits, and so on.

Let's say we group the numbers by the count of their digits. So all one-digit numbers are in the first group, all two-digit numbers are in the second group, and so on. The total number of digits in $i^{th}$ group, starting with i = 0, is $9 * (i + 1) * 10^i$, and the largest number in the group is $10^{i + 1} - 1$.

Now we can find, say, the 100th digit using a simple procedure. We know that the first group has a total of 9 digits, so subtract 9 from 100, which gives us 91. The second group has 180 digits, which is greater than 91, so the 100th digit must fall within the second group, and specifically we are looking for the 91st digit within this group.

The second group has two-digit numbers. 91 divided by 2 is 45 with a remainder of 1. So we are looking for the first digit after 45 numbers in this group. The largest number in the previous group was 9, so the 46th number of this group is 9 + 46 = 55, and the first digit of that number is 5.

We can use the same procedure to find all the other digits.
