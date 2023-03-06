'''
Exercise 10.4* (foldr)
In this exercise the goal is to make an implementation of foldr (fold right). 
Python's reduce function is often called foldl (fold left) in other programming languages, 
that given a function f and a list [x1, x2, x3, ..., xn] computes f(f(···f(f(x1, x2), x3)···), xn).

The function foldr should instead compute f(x1, f(x2, f(x3, f(···f(xn-1, xn)···)))).

This function does not appear in the Python standard library but is standard in other programming languages, 
in particular functional programming languages like Haskell and ML. The difference between folding left and 
right is illustrated by applying the power function to the list [2, 2, 2, 2], where ((2 ** 2) ** 2) ** 2 == 256
whereas 2 ** (2 ** (2 ** 2)) == 65536.

import functools
foldl = functools.reduce

def foldr(f, L):
    # your code

print(foldl(lambda x, y: x ** y, [2, 2, 2, 2]))     # prints 256
print(foldr(lambda x, y: x ** y, [2, 2, 2, 2]))     # should print 65536
print(foldr(lambda x, y: x ** y, [2, 2, 2, 2, 2]))  # value with 19729 digits
Note. You can implement foldr both with a loop and recursively.


'''

import functools
foldl = functools.reduce

def foldr(f, L): #recursive function
    if len(L) < 3: #base case: foldl of the two rightmost objects
        return foldl(f,L)
    else:
        return foldl(f,[L[0], foldr(f,L[1:])]) #recursion: use foldl with the element to the left of the elements we have already folded

print(foldl(lambda x, y: x ** y, [2, 2, 2, 2]))     # prints 256
print(foldr(lambda x, y: x ** y, [2, 2, 2, 2]))     # should print 65536
#print(foldr(lambda x, y: x ** y, [2, 2, 2, 2, 2]))  # value with 19729 digits