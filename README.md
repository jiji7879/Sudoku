# Sudoku!
#### Video Demo: https://youtu.be/YGm7vp1En7M
<br/>

#### Description:
"Sudoku!" is a program that will take in 9x9 sudokus, either through user input, a text file, or a csv file.

This was done for the CS50P final project.

---

How to run the program:

The following libraries are used in this Python folder:
- sys
- re
- copy
- tabulate (to install, use the command line "pip install -r requirements.txt")

Make sure you have a sudoku to input.
You can either put it in a .txt/.csv file, or input it manually.

The command line argument should look something like this:
 - python project.py [file.txt/file.csv]

To input each line manually, input the 9 numbers from each row. The empty spaces can either be a 0 or a space. If you make an error midway, you can type "error" to replace an existing line with a new input.

For .txt or .csv files, the program will only read the first 9 lines to input the sudoku. If the lines do not fit the input format, the file will be rejected and the program will terminate. (If you are inputting through a csv file, each value MUST be separated by a comma.)

The program will print out all solutions found (if any). If at least one solution is found, the program will ask whether you want to output the solutions to a .txt file. If you say yes, only put in the name of the file. (Example: inputting "output1" will output to "output1.txt".)

---

This project was designed to be relatively small-scale, but should effectively demonstrate the big concepts of the course. Coming into the course, I already a background on the algorithmic/backend part of programming. For my project, I wanted to emphasize both back-end and front-end (or the user experience) parts equally.

---

First, the backend. The backend involved in the algorithm for sudoku is not particularly groundbreaking, but the pseudo-code for the algorithm is as follows:
 - Check that the input is a valid sudoku problem.
 - For each "zero" or "space" in the problem, check each value one by one.
    - If the value is valid for the time being (checking its row, column, and square), go to the next "zero"
    - Once all values have been checked, go to the previous "zero"

This is definitely not the fastest algorithm solving sudokus, but it certainly is a valid (and surprisingly quick) way of doing it. In order to implement this, I had to call on a 2 dimensional list. This was briefly hinted on in the class, but there was no direct emphasis on it.

---

Most of the new things I have learned for the course has been implemented in the front end. In the project, I made it my mission to make the experience as "friendly" as possible. That really just means "If I found something inconvenient while testing, I wanted to implement a fix to it."

Some features of the front-end experience:
 - If the user forgets to input in a file, the code will first ask whether you actually want a file to be inputted
 - If the user inputs a wrong line midway, there is always an option to go back and fix the mistake.
 - If solution(s) are found, it will print it out in a very nice grid format, just like an actual sudoku.
 - If solution(s) are found, at the very end the code will ask if you want to output it to another file.

Regular expressions turn out to be very useful for checking if a user input is correct.
