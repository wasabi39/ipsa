'''
Write a program that solves the eight queens puzzle. 
The program should solve the more general problem of solving the n queen problem on an n x n chessboard, 
where n is given as input. The program should output at least one solution if solutions exist, 
e.g. as below, or that there is no solution.

Size of board: 5
Q....
..Q..
....Q
.Q...
...Q.

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
