Exercise: Basic Syntax, Conditional Statements, and Loops

Problems for exercise and homework for the Python Fundamentals Course @SoftUni. 

1.	Jenny's Secret Message
Jenny studies programming with Python and wants to create a program that greets the user when he/she gives his/her name. 
The greeting should be in the format "Hello, {name}!". However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!". 
Could you help her?

Examples
Input - 	Output
Peter	 -> Hello, Peter!  
Amy	-> Hello, Amy!  
Johnny ->	Hello, my love!

2.	Drink Something
Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. 
Create a program that receives a person's age and prints what he/she drinks.

Rules:
A kid is defined as someone under or at the age of 14.
A teen is defined as someone under or at the age of 18.
A young adult is defined as someone under or at the age of 21.
An adult is defined as someone above the age of 21.
Note: All the values are inclusive except the last one!

Examples:
Input	- Output
13	-> drink toddy  
17	-> drink coke  
21	-> drink beer  
30	-> drink whisky  

3.	Chat Codes
Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes. 
He starts by creating a program for only four messages. 
Create a program that receives the n number of messages sent. 
On the following n lines, it will receive integer numbers. 

For each number, the program should print a different message:
•	If the number is 88 - "Hello"
•	If the number is 86 - "How are you?"
•	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
•	If the number is over 88 - "Bye."

Examples:

Input:
4  
88  
86  
2  
105  

Output:
Hello  
How are you?  
GREAT!  
Bye.  

Input:
3  
88  
88  
89  

Output:
Hello  
Hello  
Bye.  

4.	Maximum Multiple
On the first line, you will be given a positive number, which will serve as a divisor. 
On the second line, you will receive a positive number that will be the boundary. 
You should find the largest integer N, that is:
•	divisible by the given divisor
•	less than or equal to the given bound
•	greater than 0
Note: it is guaranteed that N is found.

Examples:
Input:
2  
7  

Output:
6  

Input:
10  
50  

Output:
50

Input:
37  
200  

Output:
185

5.	Orders
You work at a coffee shop, and your job is to place orders to the distributors. 
Thus, you want to know the price of each order. On the first line, you will receive integer N - the number of orders the shop will receive. 

For each order, you will receive the following information:
•	Price per capsule - a floating-point number in the range [0.01…100.00]
•	Days - integer in the range [1…31]
•	Capsules, needed per day - integer in the range [1…2000]

For each order, you should print a single line in the following format:
•	"The price for the coffee is: ${price}"

If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and move to the next one.
After you go through all orders, you need to print the total price in the following format:
•	 "Total: ${total_price}"
Both the price of a coffee and the total price must be formatted to the second decimal place. 

Examples:

Input:
1  
1.53  
30  
8  

Output:
The price for the coffee is: $367.20  
Total: $367.20

Input:
2  
4.99  
31  
3  
0.35  
31  
5  

Output:
The price for the coffee is: $464.07  
The price for the coffee is: $54.25  
Total: $518.32

Input:
2  
9.223  
31  
0  
0.05  
10  
30  

Output:
The price for the coffee is: $15.00  
Total: $15.00

6.	String Pureness
You will be given number n. After that, you'll receive different strings n times. 
Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
•	If a string is pure, print "{string} is pure."
•	Otherwise, print "{string} is not pure!"

Examples:

Input:
2  
pure string  
not_pure_string  

Output:
pure string is pure.  
not_pure_string is not pure!

Input:
3  
SoftUni  
12345  
string.pureness  

Output:
SoftUni is pure.  
12345 is pure.  
string.pureness is not pure!

7.	Double Char
You will be given strings until you receive the command "End".
For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
Note that if you receive the string "SoftUni", you should NOT print it!

Examples:

Input:
Hello World  
Repeat  
End

Output:
HHeelllloo  
WWoorrlldd  
RReeppeeaatt

Input:
1234!  
SoftUni  
softuni  
End

Output:
11223344!!  
ssooffttuunnii

8.	How Much Coffee Do You Need?
Everybody knows that you spend too much time awake during nighttime.
Your task is to define how much coffee you need to stay awake. 
Until you receive the command "END", you need to read commands on different lines. 
According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
The list of events can contain the following:
•	You have homework to do ("coding").
•	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
•	You watch a movie ("movie").
•	If other events are present, they will be represented by arbitrary strings. Just ignore them!
Each event can be lowercase or uppercase:
•	If it is lowercase, you need 1 coffee by an event.
•	If it is uppercase, you need 2 coffees by an event.
In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".

Examples:

Input:  
dog  
CAT  
gaming  
END

Output:  
3

Input:  
movie  
CODING  
MOVIE  
CLEANING  
cat  
END	

Output:  
You need extra sleep

9.	Sorting Hat
Help out the sorting hat to sort the new students in the houses of Hogwarts.
You will be receiving names until the command "Welcome!". The length of each name determines in which house the student is going:
•	If the name is less than 5 chars, the student is going into Gryffindor
o	Print "{name} goes to Gryffindor."
•	If the name is exactly 5 chars, the student is going into Slytherin
o	Print "{name} goes to Slytherin."
•	If the name is exactly 6 chars, the student is going into Ravenclaw
o	Print "{name} goes to Ravenclaw."
•	If the name is more than 6 chars, the student is going into Hufflepuff
o	Print "{name} goes to Hufflepuff."
While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!
If all students are sorted successfully, print "Welcome to Hogwarts."

Examples:

Input:  
Harry  
Ron  
Ginny  
Draco  
Welcome!

Output:  
Harry goes to Slytherin.  
Ron goes to Gryffindor.  
Ginny goes to Slytherin.  
Draco goes to Slytherin.  
Welcome to Hogwarts.

Input:
Luna  
Hermione  
Neville  
Voldemort  

Output:
Luna goes to Gryffindor.  
Hermione goes to Hufflepuff.  
Neville goes to Hufflepuff.  
You must not speak of that name!
