01.Problem: Converter: from USD to BGN
Write a program to convert US dollars (USD) to Bulgarian leva (BGN). Use a fixed exchange rate between the dollar and the lev: 1 USD = 1.79549 BGN.
Sample input and output
input output   input output  input output
22    39.50078 100   179.549 12.5  22.443625
Directions
1. Read the console input (USD):
2. Create a new variable in which you will do the conversion from US dollars to Bulgarian leva, knowing the exchange rate:
3. Print the received Bulgarian leva.

02.Problem: Radians to Degrees
Write a program, that reads an angle in radians (rad) and converts it to degrees>) (deg). Look for a proper formula on the Internet. 
The number π in Python programs is available through math.pi but before that, we have to refer to the math library using import math.

input	   output             input	   output             input	   output 
3.1416	180.0004209182994		6.2832	360.0008418365988		0.7854	45.00010522957485

03.Problem: Deposit calculator
Write a program that calculates how much you will receive at the end of the deposit period at a given interest rate. Use the following formula:
amount = deposited amount + term of the deposit * ((deposited amount * annual interest rate ) / 12)
input
3 lines are read from the console:
1. Amount deposited – real number in the interval [100.00 … 10000.00]
2. Term of the deposit (in months) – an integer in the interval [1…12]
3. Annual interest rate - real number in the interval [0.00 …100.00]
output
To print the amount at the end of the term on the console.
input	output   input	output
200            2350
3              6
5.7	  202.85   7      2432.25

04.Problem: Vacation books list
There are a number of books on Joro's must-read list for summer vacation. Since Joro prefers to play with friends outside, 
your task is to help him calculate how many hours a day he should spend to read the necessary literature.
input
3 lines are read from the console:
1. Number of pages in the current book - an integer in the range [1…1000]
2. Pages read in 1 hour - an integer in the range [1…1000]
3. The number of days for which he should read the book - an integer in the range [1…1000]
output
To print on the console the number of hours Joro must spend reading each day.
input	output  input	output
212           432   7
20            15
2	    5       4

05.Problem: Supplies for school
The school year has already started and the teacher of class 10B - Annie has to buy a certain number of packets of chemicals, packets of markers, as well as blackboard cleaner. She is a regular customer of a bookstore, so there is a discount for her, which is some percentage of the total amount. Write a program that calculates how much money Annie will need to collect to pay the bill, given the following price list:
• Package of chemicals - BGN 5.80.
• Pack of markers - BGN 7.20.
• Detergent - BGN 1.20 (per liter)
input
4 numbers are read from the console:
• Number of chemical packages - an integer in the interval [0...100]
• Number of tag packets - an integer in the interval [0...100]
• Liters of chalkboard cleaner - an integer in the range [0…50]
• Percent reduction - an integer in the interval [0...100]
output
To print on the console how much money Annie will need to pay her bill.
input	output  input	output
2             4     58.68
3             5
4             5
25	  28.5    10

06.Problem: Repainting
Rumen wants to repaint the living room and has hired craftsmen for this purpose. Write a program that calculates the cost of the repair given the following prices:
• Protective nylon - BGN 1.50 per square meter
• Paint - BGN 14.50 per liter
• Paint thinner - BGN 5.00 per liter
Just in case, to the necessary materials, Rumen wants to add another 10% of the amount of paint and 2 sq.m. nylon, of course, and BGN 0.40 for bags. The amount paid to craftsmen for 1 hour of work is equal to 30% of the sum of all material costs.
input
The input is read from the console and contains exactly 4 lines:
1. Required amount of nylon (in square meters) - an integer in the interval [1... 100]
2. Required amount of paint (in liters) - an integer in the interval [1…100]
3. Amount of thinner (in liters) - an integer in the interval [1…30]
4. The hours for which the craftsmen will complete the work - an integer in the interval [1…9]
output
To print one line to the console:
• "{sum of all costs}"
input	output  input	output
10            5
11            10
4             10
8	    727.09  1     286.52

07.Problem: Food delivery
A restaurant opens its doors and offers several menus at preferential prices:
• Chicken menu – BGN 10.35.
• Fish menu – BGN 12.40.
• Vegetarian menu – BGN 8.15.
Write a program that calculates how much it will cost a group of people to order takeout.
The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery).
The delivery price is BGN 2.50 and is charged at the end.
input
3 lines are read from the console:
• Number of chicken menus - an integer in the range [0 … 99]
• Number of fish menus - an integer in the range [0 … 99]
• Number of vegetarian menus - an integer in the range [0 … 99]
output
Print one line to the console: "{order price}"
input	output  input	output
2            9      
4            2
3	    116.2  3      173.38

08.Problem: Basketball equipment
Jesse decides he wants to play basketball, but he needs equipment to practice. Write a program that calculates what costs Jesse will incur if he starts coaching, knowing the cost of basketball coaching over a 1-year period. Required equipment:
• Basketball shoes - their price is 40% less than the fee for one year
• Basketball team - its price is 20% cheaper than sneakers
• Basketball – its price is 1/4 of the price of the basketball team
• Basketball accessories – their price is 1 / 5 of the price of the basketball
input
1 line is read from the console:
• The annual fee for basketball training - an integer in the range [0… 9999]
output
To print on the console what Jesse's expenses will be if he starts playing basketball.
input	output  input	 output
365	  811.76  550    1223.2

09.Problem: Aquarium
For his birthday, Lubomir received an aquarium in the shape of a parallelepiped. Initially, we read from the console in separate lines its dimensions - length, width and height in centimeters. It is necessary to calculate how many liters of water the aquarium will collect, if it is known that a certain percentage of its capacity is occupied by sand, plants, heater and pump.
One liter of water equals one cubic decimeter/ 1l=1 dm3/.
Write a program that calculates the liters of water needed to fill the aquarium.
Login
4 lines are read from the console:
1. Length in cm – an integer in the range [10 … 500]
2. Width in cm – an integer in the interval [10 … 300]
3. Height in cm - an integer in the range [10… 200]
4. Percentage – a real number in the interval [0.000 … 100.000]
Exit
To print a number to the console:
• the liters of water that the aquarium will collect.
input	output       input output
85                 105
75                 77
47                 89
17	  248.68875    18.5  586.445475







