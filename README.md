# Contents
- [Problem Statement](#problem-statement)
- [Examples](#examples)
  - [N = 4](#example-2-n--4)
  - [N = 5](#example-2-n--5)
  - [N = 6](#example-2-n--6)
- [Approaches](#approach)
  - [Approach 1: Bit Manipulation](#approach-1---bit-manipulation)
  - [Approach 2: Dynamic Programming](#approach-1---bit-manipulation)
    - [Approach A - O(N) Space Complexity](#dynamic-programming---approach-a)
    - [Approach B - O(1) Space Complexity](#dynamic-programming---approach-b)
- [How to run](#how-to-run-the-program)

# Problem Statement

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: **14/29**

for 10 days: **372/773**

--------------------------------------------------------------

# Examples

## Example 1: N = 4

Lets consider 0 as Absent and 1 as Present

```
Total ways to attend the college are as follows:

0000 0001 0010 0011

0100 0101 0110 0111

1000 1001 1010 1011

1100 1101 1110 1111
```

**Therefore, count of total ways to attend the college = 16 = 2^4**

```
Invalid ways to attend the college:
There should be four or more consecutive absence

0000

1 invalid way
```


**Therefore, count of total valid ways to attend the college: 16-1 = 15**

```
Ways in which graduation ceremony will be missed:
If the student misses last day of college, he would miss graduation ceremony


0010

0100 0110

1000 1010

1100 1110
```

**Therefore, count of ways in which student misses his graduation ceremony = 7**

### For N=4, Answer: 7/15


## Example 2: N = 5

Lets consider 0 as Absent and 1 as Present

```
Total ways to attend the college are as follows:

00000 00001 00010 00011

00100 00101 00110 00111

01000 01001 01010 01011

01100 01101 01110 01111

10000 10001 10010 10011

10100 10101 10110 10111

11000 11001 11010 11011

11100 11101 11110 11111
```

**Therefore, count of total ways to attend the college = 32 = 2^5**

```
Invalid ways to attend the college:
There should be four or more consecutive absence

00000 00001

10000

3 invalid ways
```


**Therefore, count of total valid ways to attend the college: 32 - 3 = 29**

```
Ways in which graduation ceremony will be missed:
If the student misses last day of college, he would miss graduation ceremony

00010

00100 00110

01000 01010

01100 01110

10010

10100 10110

11000 11010

11100 11110
```

**Therefore, count of ways in which student misses his graduation ceremony = 14**

### For N=5, Answer: 14/29


## Example 3: N = 6

Let's consider 0 as Absent and 1 as Present

```
Total ways to attend college are as follows:

000000 000001 000010 000011 000100 000101 000110 000111

001000 001001 001010 001011 001100 001101 001110 001111

010000 010001 010010 010011 010100 010101 010110 010111

011000 011001 011010 011011 011100 011101 011110 011111

100000 100001 100010 100011 100100 100101 100110 100111

101000 101001 101010 101011 101100 101101 101110 101111

110000 110001 110010 110011 110100 110101 110110 110111

111000 111001 111010 111011 111100 111101 111110 111111
```

**Therefore, the count of total ways to attend college = 64 = 2^6**

```
Invalid ways to attend college:
There should be four or more consecutive absences.

000000 000001 000010 000011

010000

100000 100001

110000

8 invalid ways
```

**Therefore, the count of total valid ways to attend college: 64 - 8 = 56**

```
Ways in which the graduation ceremony will be missed:
If the student misses the last day of college, they would miss the graduation ceremony.

000100 000110

001010 001100 001110

010000 010010 010100 010110

011000 011010 011100 011110

100010 100100 100110

101000 101010 101100 101110

110010 110100 110110

111000 111010 111100 111110
```

**Therefore, the count of ways in which the student misses the graduation ceremony = 27**

### For N = 6, Answer: 27/56

# Approach

## Approach 1 - Bit Manipulation

For a particular N, we have 2 power N total ways.

We can iterate over all 2^N total ways and find if a way `i` is a valid way.
If way `i` is a valid way, check if the student would miss grad ceremony if he goes that way.


**How to find valid way?**

Suppose there is a way `x`. In our case, `x` will be in the range [0, 2^N) since there are 2^N ways.

Now, for the integer `x`, check if it has 4 or more consective bits set.
If yes, then it is an invalid way. Otherwise, a valid way

**How to check if student would miss graduation cermeony?**

Suppose, `x` is found to be a valid way.

To figure out, if the grad would miss the graduation ceremony,
the last bit in `x` should be unset.

Therefore, for a valid way, if the last bit is unset,
the student would not be able to attend the graduation ceremony.


**Time Complexity: O(2^N)**

**Space Complexity: O(1)**



## Approach 2 - Dynamic Programming

Let's check answers for N=1 till N=6 

N = 1
------
All ways -> 0, 1

Valid ways -> 0, 1

No. of valid ways to attend college = 2
Graduation miss chances = 1

Therefore, answer is 1/2


N = 2
-------
All ways -> 00, 01, 10, 11

Valid ways -> 00, 01, 10, 11

No. of valid ways to attend college = 4
Graduation miss chances = 2

Therefore, answer is 2/4


N = 3
-------
All ways -> 000, 001, 010, 011, 100, 101, 110, 111

Valid ways -> 000, 001, 010, 011, 100, 101, 110, 111

No. of valid ways to attend college = 8
Graduation miss chances = 4

Therefore, answer is 4/8


N = 4
-------
All ways -> 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111

Valid ways -> 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111

No. of valid ways to attend college = 15
Graduation miss chances = 7

Therefore, answer is 7/15



N = 5
-------

Now, from the [example](#example-2-n--5) that we saw above, for N=5, Answer is 14/29

If we observe,
No. of valid ways to attend college for N=5 is sum of valid days for (N=1, N=2, N=3, N=4) = 2+4+8+15 = 29
Grad miss chances for N=5 is sum of grad miss chances for (N=1, N=2, N=3, N=4) = 1+2+4+7 = 14

Therefore, answer is 14/29


N = 6
------

Now, from the [example](#example-2-n--6) that we saw above, for N=6, Answer is 27/56

No. of valid ways to attend college = 4 + 8 + 15 + 29 = 56 (Sum valid ways for N=2, N=3, N=4, N=5)
Graduation miss chances = 2 + 4 + 7 + 14 = 27 (Sum graduation ceremony miss chances for N=2, N=3, N=4, N=5)

Here, we can observe we can break a particular N into smaller sub-problem
We can observe that the number of valid ways to attend the class depends on the valid ways
to attend classes on previous 4 days.

Similarly, the no. of ways to miss grad ceremony is also depending on the the no. of ways grad ceremony
can be missed on previous 4 days

Thus, dynamic programming approach works here.

## Dynamic Programming - Approach A
Store the base cases N=0 to N=4 in the list L and then keep calculating further
and then keep on appending the valid ways till the required N to the list.
Finally, return L[N]

There would be 2 lists: One for no. of valid ways and another for no. of ways to miss graduation ceremony

**Time Complexity = O(N)**

**Space Complexity = O(N)**

## Dynamic Programming - Approach B
Since we need previous information i.e. for N=5, we need information about N=1 to N=4,
we can create 4 variables which stores the information about valid ways and graduation ceremony miss chances.
We store N-4, N-3, N-2 and N-1 in prev1, prev2, prev3 and prev4 respectively and keep on updating.

By this approach, we can improve upon Space Complexity

**Time Complexity = O(N)**

**Space Complexity = O(1)**


# How to Run the program

**Prerequisite**: Python 3 must be installed in your local machine.

To run the assignment execute following command:

```
python3 main.py 5
```

Here 5 is the number of days, value for N.
