'''One way to structure your program is to define three functions:

valid(r1, c1, r2, c2) that checks if two queens at positions (r1, c1) and (r2, c2) 
respectively do not threaten each other (i.e. are in different rows and columns and not on the same diagonal).

print_solution(solution) that prints a solution given by a list solution where 
queen i is at position (i,solution(i)).

solve(solution) is a recursive function that tries to expand a partial solution 
given by solution for the first len(solution) queens.

'''
import time

def valid(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return False
    elif c1 - r1 == c2 - r2 or c1 - r2 == c2 - r1:
        return False
    else:
        return True
    
def print_solution(n, l):
    for row in range(n):
        board_row = ''
        for column in range(n):
            if l[row] == column:
                board_row += 'Q '
            else:
                board_row += '▢ '
        print(board_row)

counter = 0
def solve(n, solution = 'a'):
    if isinstance(solution, list) != True:
        solution = []
        for q in range(n):
            solve(n, [q])
    elif len(solution) < n:
        for column in range(n):
            valid_solution = True
            for queen in range(len(solution)):
                if valid(queen,solution[queen],len(solution), column) == False:
                    valid_solution = False
            if valid_solution == True:
                new_solution = solution + [column]
                solve(n, new_solution)
    else:
        print_solution(n, solution)
        global counter
        counter += 1
        print(counter)

solution_printed = False

def solve_one_solution(n, solution = 'a'):
    if isinstance(solution, list) != True:
        solution = []
        for q in range(n):
            solve_one_solution(n, [q])
    elif len(solution) < n:
        for column in range(n):
            valid_solution = True
            for queen in range(len(solution)):
                if valid(queen,solution[queen],len(solution), column) == False:
                    valid_solution = False
            if valid_solution == True:
                new_solution = solution + [column]
                solve_one_solution(n, new_solution)
    else:
        global solution_printed
        if solution_printed == False:
            print_solution(n, solution)
            solution_printed = True
        global counter
        counter += 1

def solve_n_queens():
    if input("Do you want to print all solutions (y/n)?") in ["yes","y"]:
        n = int(input('Please enter the value of n you want to solve for:'))
        st = time.time()
        solve(n)
        et = time.time()
        print("The number of solutions for n=" + str(n) + " is equal to " + str(counter) + ".")
        print("Time to calculate solutions: " + str(round(et - st, 2)) + " seconds.")
        
    else:
        n = int(input('Please enter the value of n you want to solve for:'))
        st = time.time()
        solve_one_solution(n)
        et = time.time()
        print("The number of solutions for n=" + str(n) + " is equal to " + str(counter) + ".")
        print("Time to calculate solutions: " + str(round(et - st, 2)) + " seconds.")

solve_n_queens()
