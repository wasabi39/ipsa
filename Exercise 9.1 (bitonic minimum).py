'''
Exercise 9.1 (bitonic minimum)
We call a list L = [x1, ..., xn] bitonic, if there exists a k, 1 < k < n, such that

x1 > x2 > ··· > x{k-1} > xk < x{k+1} < ··· < xn,
i.e. xk is the minimum of the list. Write a method bitonic_min that given a bitonic list, 
returns the minimum of the list. Your implementation should use binary search 
(i.e. you cannot use the Python builtin min function).

Example. bitonic_min([10, 7, 4, 2, 3, 5, 9, 11, 13, 15]) should return 2.

'''
def bitonic_minimum(l):
    if isinstance(l, int): #på vej ud af rekursionen returnerer vi bare det ene element
        return l
    elif len(l) < 2: #returnerer det eneste element i rekursionen, når vi kun har et element tilbage
        return l[0]
    elif l[len(l) // 2] < l[len(l) // 2 - 1]: #tjekker om venstre halvdel indeholder det mindste element
        return bitonic_minimum(l[len(l) // 2:])
    else: #ellers bruger vi højre halvdel
        return bitonic_minimum(l[:len(l) // 2])

print(bitonic_minimum([10, 7, 4, 2, 3, 5, 9, 11, 13, 15]))
