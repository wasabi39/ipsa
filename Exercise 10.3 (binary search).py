'''
Exercise 10.3 (binary search)
Assume you have a function f mapping integers to True and False, and there exists an integer x such that f(y) == False 
for y < x, and f(y) == True for y ≥ x. Write a function binary_search(f, low, high) that returns the smallest x where 
f(x) == True, provided f(low) == False and f(high) == True. The function should use binary search, like 
in Exercise 9.1 (bitonic minimum).

Example. binary_search(lambda x: x * x >= 1000, 0, 1000) == 32 == ceil(sqrt(1000)).

Assume now f is a function from floats to floats that is strictly decreasing in an interval [low, x_min] and strictly
increasing in the interval [x_min, high] for some real number x_min and integers low and high. Use your function binary_search 
to write a function local_min(f, low, high) that returns the smallest integer x in the range ]low, high] such that 
f(x) < f(x + 1), i.e. a local minimum of f.

Example. local_min(lambda x: (x - 3.5) ** 2 - 7 * x, -1000, 1000) returns 7.


'''

def binary_search(f, low, high):
    if low == high or high - low == 1:
        return high
    else:
        if f((low + high) // 2) == False:
            return binary_search(f, (low + high) // 2, high)
        else:
            return binary_search(f, low, (low + high) // 2)

print(binary_search(lambda x: x * x >= 1000, 0, 1000)) #bør returnere 32
print(binary_search(lambda x: x * x * x >= 1000, 0, 1000)) #bør returnere 10

def local_min(f, low, high):
    if low == high or high - low == 1:
        return high
    else:
        if f((low + high) // 2) < f((low + high) // 2 + 1): #hvis det lige til højre for midten større end midten, må min ligge i venstre side
            return local_min(f, low, (low + high) // 2)
        else: #ellers må det ligge i højre side
            return local_min(f, (low + high) // 2, high)

print(local_min(lambda x: (x - 3.5) ** 2 - 7 * x, -1000, 1000)) #bør returnere 7