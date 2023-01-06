'''
Inputs : 

g = [g_0, ... g_n]
s = [s_0, ... s_n]

Output :
 
G = g_0*s_0 + ... + g_1*s_1
'''

import random

## Example
SIZE = 11
g = [random.randint(0, 9) for i in range(SIZE)]
g_id = 0
##

def g_mult_scalar(a, b):
    return a * b

def g_add_scalar(a, b):
    return a + b

def mexp(s):
    res = g_id
    for i in range(SIZE):
        gms = g_mult_scalar(s[i], g[i])
        res = g_add_scalar(res, gms)
    return res

s = [random.randint(0, 9) for i in range(SIZE)]

print("---------------------------")
print("Multi-Scalar-Multiplication")
print("---------------------------\n")

print("Group g = " + str(g) + "\nGroup s = " + str(s) + "\n")

print("MSM of group g with s : \nexp_g(s) = " + str(mexp(s)) + "\n")

print("---------------------------")
print("---------------------------\n")