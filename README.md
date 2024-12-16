# Intro-to-Prog-Python-Module08
Assignment 08
# Application Documentation
This document gives a brief explanation of the multimodule application to enter employee rating data. 

## Writing code

In this program, I have used the separation of concerns method and divided my code into 4 modules:
1. **Data Module**: This data layer is responsible for handling data-related operations such as data storage and retrieval. 
2. **Processing Module**: This module is responsible for implementing the core functionality and processes and transforms data as required by the application.
3. **IO/Presentation Module**: This I/O layer focuses on presenting information to users and capturing user input.
4. **Main Module**: All the above classes are linked to the "main" file which gets access to all of their functions and classes using the "Import" function


The below component diagram shows the logical components of the application and their dependencies. ![](../images/UML.png)

_____
## Testing
Unit Testing is used to evaluate each individual unit of code to ensure if they function correctly in isolation. Python's unittest framework is very useful in running such unit tests. The code starts by importing the unittest module, which provides the testing framework for creating and running test cases.

Below is a screenshot of Unit test code the class Person

![](../images/unit%20test.png)

-----
## Output
The output of the application was as desired.

Output for menu choice 1

![](..%2Fimages%2FOutput%20menu%20choice%201.png)

Output for menu choice 2

![Output menu choice 2.png](..%2Fimages%2FOutput%20menu%20choice%202.png)

Output for menu choice 3 and 4

![output menu choice 3 and 4.png](..%2Fimages%2Foutput%20menu%20choice%203%20and%204.png)

 
