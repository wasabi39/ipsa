'''
Exercise 10.1 (my_map)
In this exercise the goal is make your own implementation of Python's builtin map function.

Make a function my_map that takes two arguments, a function f and a list [x1, ..., xn], and returns the list [f(x1), ..., f(xn)].

Example. my_map(lambda x: x ** 3, [3, 2, 4])) should return [27, 8, 64].

Make a function my_map_k that as arguments takes a function f requiring k ≥ 1 arguments and k lists L1, ..., Lk, 
and returns the list [f(L1[0], ..., Lk[0]), ..., f(L1[n-1], ..., Lk[n-1])], where n is the length of the shortest Li list.

Hint. Use Python's * notation to handle an arbitrary number of lists as arguments.

Example. my_map_k(lambda x, y, z: x * y * z, [3, 2, 5], [2, 7, 9], [1, 2]) should return [6, 28].

Note. Your solution should not use the builtin map function.


'''
#delopgave a
def my_map(f, l):
    return [f(n) for n in l] #vi bruger list comprehension med funktionen taget på hvert element i listen

print(my_map(lambda x: x ** 3, [3, 2, 4]))

#delopgave b
def my_map_k(f,*l):
    max_len = 999999999999
    for k in l:
        if len(k) < max_len:
            max_len = len(k)
    return_list = []
    for n in range(max_len):
        temp_list = []
        for m in l:
            temp_list.append(m[n])
        return_list.append(f(tuple(temp_list)))
    return return_list

    
    #return [f(sub_list) for sub_list in [k[0] for k in l]]

print(my_map_k(lambda x, y, z: x * y * z, [3, 2, 5], [2, 7, 9], [1, 2]))