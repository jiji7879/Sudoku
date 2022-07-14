from tabulate import tabulate
import sys
import re
import copy
import csv

def main():
    #check for argument size
    #get the sudoku grid
    if len(sys.argv) > 3:
        print("Too many command line arguments.")
        print("Pass in nothing to input your own sudoku")
        sys.exit("Or pass in a .txt or .csv file to parse an existing sudoku.")
    elif len(sys.argv) == 1:
        grid = argv1()
    elif len(sys.argv) == 2:
        grid = argv2(sys.argv[1])

    #from the grid, check exactly where the zeros are
    zeros_list = zeros(grid)

    #check if the input is valid
    if initialcheck(grid, zeros_list) == False:
        sys.exit("Input is not a valid sudoku problem!")

    if len(zeros_list) == 0:
        sys.exit("This sudoku has already been filled!")
    #solve the sudoku
    #gives a list of solutions and prints them in a table
    solutions = forcesolution(grid, zeros_list)
    #outputs the solutions if prompted
    outputsolutions(solutions)

def argv1():
    #Ask either file (y), input (n), or exit (e)
    #Loop if not
    while True:
        if matches := re.search(r"^(y|n|e)", \
                input("Would you like to input a file? (y)es for file, (n)o for manual input, or (e)xit "), re.IGNORECASE):
            break
    if matches[1] == "y":
        filename = input("What is the filename? ")
        grid = argv2(filename)
        return grid
    elif matches[1] == "e":
        sys.exit("Exiting.")

    #Either 9 numbers, "exit", or "error"
    grid = []
    i=0
    while len(grid) < 9:
        #Gives 10 groups. 9 for numbers, 1 for "error"
        if matches := re.search(r"^(?:(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| )|exit|(error))$", \
                input(f"Row {i+1}: Input a row, or type 'exit'. If you made a mistake, type 'error'. "), re.IGNORECASE):
            row = []
            if matches.groups()[9] == "error":
                error(grid)
                continue
            for character in matches.groups()[0:9]:
                if character == None:
                    sys.exit("Exiting.")
                elif character == " ":
                    row.append(0)
                else:
                    row.append(int(character))
            grid.append(row)
            i+=1
        else:
            print(f"Input does not follow the format of 9 numbers (or 1-9 with spaces for empty cell).")
    return grid

def error(grid):
    i=1
    for row in grid:
        rowstring = ""
        for number in row:
            rowstring += str(number)
        print(f"Row {i}: {rowstring}")
        i+=1
    while True:
        try:
            rownumber = int(input("Which line has the error? Type '0' if no error. "))
            if rownumber < 0 or rownumber > len(grid):
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Must be an integer with corresponding row number or '0'.")
    if rownumber == 0:
        return grid
    if matches := re.search(r"^(?:(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| )|exit)$", \
            input(f"Row {rownumber}: Input a row, or type 'exit'. "), re.IGNORECASE):
        row = []
        for character in matches.groups():
            if character == None:
                sys.exit("Exiting.")
            elif character == " ":
                row.append(0)
            else:
                row.append(int(character))
        grid[rownumber-1] = row
    else:
        print(f"Input does not follow the format of 9 numbers (or 1-9 with spaces for empty cell).")
    return grid


def argv2(filename):
    #Check for extension
    #Get first 9 lines
    #See if lines fit the format
    grid = []
    filename = filename.lower()
    #First nine lines
    if filename.endswith(".txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                if len(lines) < 9:
                    sys.exit("Not enough lines for a sudoku!")
                lines = lines[0:9]
        except FileNotFoundError:
            sys.exit("File was not found.")
        #Check lines fit the format
        i=1
        for line in lines:
            if matches := re.search(r"^(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| ),?(\d| )$", line.rstrip()):
                row = []
                for character in matches.groups():
                    if character == " ":
                        row.append(0)
                    else:
                        row.append(int(character))
                grid.append(row)
                i+=1
            else:
                sys.exit(f"Row {i} does not follow the format of 9 numbers (or 1-9 with spaces for empty cell).")
    elif filename.endswith(".csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                #j tracks first 9 lines
                j=1
                for row in reader:
                    if j > 9:
                        break
                    if len(row) != 9:
                        sys.exit(f"Row {j} does not follow the format of 9 numbers (or 1-9 with spaces for empty cell).")
                    row2 = []
                    #i tracks format
                    for i in range(9):
                        try:
                            if row[i] == " ":
                                row2.append(0)
                            else:
                                if int(row[i]) >= 10 or int(row[i]) < 0:
                                    raise ValueError
                                row2.append(int(row[i]))
                        except ValueError:
                            sys.exit(f"Row {j} has an invalid value!")
                    grid.append(row2)
                    j+=1
                if len(grid) <= 8:
                    sys.exit("Not enough lines for a sudoku!")
        except FileNotFoundError:
            sys.exit("File was not found.")
    return grid

def zeros(grid):
    zeros_list = []
    i=0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 0:
                zeros_list.append((i, j))
            j+=1
        i+=1
    return zeros_list

def initialcheck(grid, zeros_list):
    for i in range(9):
        for j in range(9):
            tuple = (i, j)
            if tuple not in zeros_list:
                if not row_check(grid, tuple) or \
                        not column_check(grid, tuple) or \
                        not square_check(grid, tuple):
                    return False
    return True

def row_check(grid, tuple):
    if grid[tuple[0]].count(grid[tuple[0]][tuple[1]]) > 1:
        return False
    return True

def column_check(grid, tuple):
    columnvalues = []
    for i in range(len(grid)):
        columnvalues.append(grid[i][tuple[1]])
    if columnvalues.count(grid[tuple[0]][tuple[1]]) > 1:
        return False
    return True

def square_check(grid, tuple):
    squarevalues = []
    #categorizes which square the tuple is at
    x = tuple[0] // 3
    y = tuple[1] // 3
    for i in range(3):
        for j in range(3):
            squarevalues.append(grid[3*x+i][3*y+j])
    if squarevalues.count(grid[tuple[0]][tuple[1]]) > 1:
        return False
    return True

def forcesolution(grid, zeros_list):
    i=0
    solutions = []
    while 0 <= i <= len(zeros_list):
        if i == len(zeros_list):
            print(tabulate(grid, tablefmt="grid"))
            solutions.append(copy.deepcopy(grid))
            i-=1
        grid[zeros_list[i][0]][zeros_list[i][1]] += 1
        if grid[zeros_list[i][0]][zeros_list[i][1]] == 10:
            if i == 0:
                break
            else:
                grid[zeros_list[i][0]][zeros_list[i][1]] = 0
                i -= 1
                continue
        if row_check(grid, zeros_list[i]) and column_check(grid, zeros_list[i]) and square_check(grid, zeros_list[i]):
            i += 1
    return solutions

def outputsolutions(solutions):
    if len(solutions) == 0:
        print("No solutions found!")
    else:
        if matches := re.search(r"^(y|n)", \
                input("Would you like to output the solution(s) to a .txt file? (y)es for file, any other letter to exit. "), re.IGNORECASE):
            if matches[1] == "y":
                print("Where would you like to output the solutions?")
                print("We will output the solutions in a .txt file")
                print("For example, an input like 'a' will output to 'a.txt'.")
                print("Note that if the output .txt file exists in this directory, it will override any data saved on it.")
                while True:
                    if outputfile := re.search(r"^([\w\-. ]+)$", input("Type in a file name: ")):
                        break
                fulloutputfile = outputfile[1] + ".txt"
                with open(f"{outputfile[1]}.txt", "w") as file:
                    for solution in solutions:
                        for line in solution:
                            numstring = ""
                            for number in line:
                                numstring += str(number)
                            file.write(f"{numstring}\n")
                        file.write("\n")

if __name__ == "__main__":
    main()
