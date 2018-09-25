Natalie DellaMaria
CPSC3600 Project 1 - Intro to Python

In my design, the program being an indefinite loop, repeatedly asking the user for input from test cases. Specifically, it reads in Throughput, RTT, and Connection Status values for each test case. It then validates that the value is a float and non negative. The read in values are stored in an instance of the TestResultContainer class. This class has an attribute called "results" that is a dictionary with the keys as the value type (throughput, rtt, and connection status) and the values as lists containing the entered data for each type of value. It continues looping and keeping track of the number of test cases entered until the user hits CTRL+C which ends the infinate loop. 

Then, functions are called on the TestResultContainer to calculate the mean and standard deviation for each of the data types. The TestResultContainer class contains two dictionaries to contain the results of the statistic calculations. The keys are the types of values (throughput, rtt, and connection status). The values are the calculated statistic (either mean or standard deviation depending on the dictionaty). 

The main program then reads from these dictionaries and prints out the results of the calculations on the inputted data. 

Finally, the results are send to a json file using a function called from the TestResultContainer. 

Overall, my implementation works and is decently efficient. Some areas of improvement include:
- my program throws an error if the user hits CRTL+C before the minimum number of values needed to calculate the mean or standard deviation are read in (need at least 2 values)
- instead of three different functions to add the three different types of values to the dictionary in TestResultContainer, I could have one fuction that contains a parameter with the type of value. This would simplify my code and potentially make it cleaner. 

Evaluation Test Case #1 Output:
You have entered 3 test results
The average and standard deviation of Throughput are 3.833 and 1.504.
The average and standard deviation of RTT are 11.033 and 1.002.
The average and standard deviation of Connection Status are 25.6 and 1.682.

Evaluation Test Casse #2 Output:
You have entered 6 test results
The average and standard deviation of Throughput are 3.755 and 1.034.
The average and standard deviation of RTT are 14.325 and 4.394.
The average and standard deviation of Connection Status are 20.692 and 5.822.