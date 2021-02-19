1.
Name:	Daniel Sanchez
CWID:	10840844

2.
The programming language used is Python.
Specifically, the version is 3.8.2.

3.
Any operating system capable of running Python3 will be able to run this program. 
I have ran the program on the following operating systems:
Windows 10
Linux: Ubuntu 20.04

4.
The "find_route" directory has two .py files that make up the code.

graph.py which contains the Node and Graph class.
	- The node class represents each "node" or "city" and has a map
	  that contains the edges or "connections" between cities.
	- The graph class represents the data structure as a whole

main.py which runs the bulk of the program and has the UCS algorithm
	- Responsible for reading and handling user arugments.
	- Creates graph object and runs UCS algorithm.
	- Based on algorithm's output, handles command line output.
NOTE: more information about each class and method is in the code comments.

5. 
To run the code, perform the following steps.

1. Set current directory to "find_route" directory
2. Run "main.py" python program with relevant arguments using python3 command
EXAMPLE:
	$ cd find_route
	$ python3 main.py input1.txt Munich Luebeck
