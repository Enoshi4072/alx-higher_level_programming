Toggle navigation
You just released the advanced tasks of this project. Have fun!
0x01. Python - if/else, loops, functions
In a nutshell…
Auto QA review: 0.0/160 mandatory & 0.0/41 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%


Resources
Read or watch:

More Control Flow Tools (Read until “4.6. Defining Functions” included)
IndentationError
How To Use String Formatters in Python 3
Learn to Program
Learn to Program 2 : Looping
Pycodestyle – Style Guide for Python Code
man or help:

python3
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How is Python’s for different from C‘s?
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
C Scripts
Allowed editors: vi, vim, emacs
All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded
More Info
Note: you do not need to understand lists yet.

Quiz questions
Great! You've completed the quiz successfully! Keep going!
Question #0
What do these lines print?

for i in range(2, 10, 2):
    print(i, end=" ")

2 3 4 5 6 7 8 9 10


2 4 6 8


2 3 4 5 6 7 8 9


4 6 8 10 12 14 16 18

Question #1
What do these lines print?

if True:
    print("Holberton")
else:
    print("School")

School


Holberton

Question #2
What do these lines print?

if 12 == 48/4:
    print("Holberton")
else:
    print("School")

School


Holberton

Question #3
What do these lines print?

for i in range(4):
    print(i, end=" ")

1 2 3 4


0 1 2 3 4


1 2 3


0 1 2 3

Question #4
What do these lines print?

if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")

School


Holberton

Question #5
What do these lines print?

a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")

Holberton


C is fun


School

Question #6
What do these lines print?

if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")

School


Holberton

Question #7
What do these lines print?

for i in range(2, 4):
    print(i, end=" ")

2 4


3 4


2 3


2 3 4

Question #8
What do these lines print?

a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")

Holberton


C is fun


School

Tasks
0. Positive anything is better than negative nothing
mandatory
Score: 0.0% (Checks completed: 0.0%)
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random. randint do. Please do not touch this code
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 0-positive_or_negative.py
    
1. The last digit
mandatory
Score: 0.0% (Checks completed: 0.0%)
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

You can find the source code here
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 1-last_digit.py
    
2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 2-print_alphabet.py
    
3. When I was having that alphabet soup, I never thought that it would pay off
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

Print all the letters except q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 3-print_alphabt.py
    
4. Hexadecimal printing
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x01-python-if_else_loops_functions
File: 4-print_hexa.py
 
