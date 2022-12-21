Exercise: Data Types and Variables

Problems for exercise and homework for the Python Fundamentals Course @SoftUni. 

1.	Integer Operations
Write a program that reads four integer numbers. 
It should add the first to the second number, integer divide the sum by the third number, and multiply the result by the fourth number. 
Print the final result.

Examples:

Input:
10
20
3
3	

Output:
30

Input:
15
14
2
3	

Output:
42

2.	Chars to String
Write a function that receives 3 characters. Concatenate all the characters into one string and print it on the console.

Examples:
Input:
a
b
c

Output:
abc

Input:
%
2
o	

Output:
%2o

Input:
1
5
p

Output:
15p

3.	Elevator
Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons. 
The input holds two lines: the number of people N and the capacity P of the elevator.

Examples:

Input:	
17
3

Output:
6

Comments:
5 courses * 3 people
+ 1 course * 2 persons

Input:
4
5

Output:
1

Comments:
All the persons fit inside the elevator.
Only one course is needed.

Input:
10
5

Output:
2

Comments:
2 courses * 5 people

Hints:
•	You should integer divide N by P. This gives you the number of full courses (e.g., 17 / 3 = 5).
•	If N does not divide without a remainder, you will need one additional partially full course (e.g., 17 % 3 = 2).
•	Another approach is to round up N / P to the nearest integer (ceiling), e.g., 17/3 = 5.67 -> rounds up to 6.
•	For the round-up calculation, you might use math.ceil() function. Before you use it, you need to import the math library: `import math`
 
 
4.	Sum of Chars
Write a program, which sums the ASCII codes of N characters and prints the sum on the console. 
On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter per line.
Print the total sum in the following format: "The sum equals: {total_sum}".

Note: n will be in the interval [1…20].

Examples:

Input:
5
A
b
C
d
E	

Output:
The sum equals: 399

Input:
12
S
o
f
t
U
n
i
R
u
l
z
z

Output:
The sum equals: 1263

5.	Print Part of the ASCII Table
Write a program that prints part of the ASCII table characters on the console, separated by a single space.
On the first line of input, you will receive the char index you should start with. On the second line - the index of the last character you should print.

Examples:

Input:
60
65

Output:
< = > ? @ A

Input:
69
79

Output:
E F G H I J K L M N O

Input:
97
104	

Output:
a b c d e f g h

Input:
40
55

Output:
( ) * + , - . / 0 1 2 3 4 5 6 7

6.	Triples of Latin Letters
Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

Examples:

Input:
3	

Output:
aaa
aab
aac
aba
abb
abc
aca
acb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc

Input:
2

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb

Hints:
•	Perform 3 nested loops from 0 to N:
 
•	For each iteration, you should generate new letters:
 
7.	Water Overflow
You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow.
On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

Examples:

Input:
5
20
100
100
100
20

Output:
Insufficient capacity!
240

Input:
1
1000

Output:
Insufficient capacity!
0

Input:
7
10
20
30
10
5
10
20

Output:
105

Input:
4
250
10
20
40

Output:
Insufficient capacity!
Insufficient capacity!
Insufficient capacity!
250
