Aim:
To write a python program to
Find LCM & HCF of two numbers.
Compute LCM Using GCD.
Find Factors of a Number using for Loop.
Find GCD of two numbers using Euclidean algorithms.
Objective:
1. To familiarize with factoring methods.
2. To write a python program to find prime factors, GCD, LCM, and HCF of a given number. 
Simulation Tool:
Python 3.11
Theory:
Algorithm :

5 (A) : Write the Python Program to Find LCM of two numbers. 
Step 1: Start
Step 2 : Find the larger of the two numbers, x and y, and store it in a variable named greater
Step 3 : Start a while loop and inside the loop, check if greater is perfectly divisible by both x and y. 
Step 4 : If the condition is true, greater is the LCM. Exit the loop and return greater
Step 5 : If the condition is false, increment greater by 1 and continue to the next iteration of the loop.
Step 6 : End

5 (B) : Write the Program to Compute LCM Using GCD.
Step 1 : Start
Step 2 : Import math module
Step 3 : Define a function as find_lcm(num1, num2)
Step 4 : If num1 == 0 or num2 == 0 then return 0
Step 5 : Calculate GCD as gcd_val = math.gcd(num1, num2)
