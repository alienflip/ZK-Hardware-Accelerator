'''
There are infinitely many finite fields, they all have a number of elements p^n (p is prime, n is an integer)

Two finite fields of the same sizes are isomorphic : they have an isomorphism between them : they have structure preseving mapping between them, and an inverse

Field with p^n elements is represented by GF(p^n) : GF(p) is the ring of integers mod p : addition, subtraction, multiplication can be perfomed, followed by reductiuon mod p 

Elements of GF(p^n) can be represented as polynomials (degree < n) over GF(p) : operations are performed mod R : R is an irreducible polynomial (degree n)

AES : fixed irreducible poly. of degree 8 over F_2^8 : x8 + x4 + x3 + x1 + 1
'''

import random

## Example
N = 8
p = 2
polynomial_0 = [random.randint(0,1) for i in range(N)]
polynomial_1 = [random.randint(0,1) for i in range(N)]
fixed_irreducible_polynomial = [1, 1, 0, 1, 0, 0, 0, 0]
irreducible_leading_term_index = 3
##

# readability helper

def to_human_readable(poly):
    poly_string, counter = [], 0
    for i in poly:
        if i == 1:
            poly_string.append("x^" + str(counter) + " ")
        counter = counter + 1
    function_string = ""
    for i in range(len(poly_string)):
        if i < len(poly_string) - 1:
            function_string = function_string + poly_string[i] + "+ "
        if i == len(poly_string) - 1:
            function_string = function_string + poly_string[i]
    return function_string

# Galois Field Add Polynomials

def add_polynomials(polynomial_0, polynomial_1):
    return [(polynomial_0[i] + polynomial_1[i]) % 2 for i in range(len(polynomial_0))]

# Galois Field Multiply Polynomials

def multiply_polynomials(polynomial_0, polynomial_1):
    polynomials_multiplied = [0 for i in range(2*N)]
    for i in range(N):
        for j in range(N):
            index = i + j 
            coefficient = polynomial_0[i] * polynomial_1[j]
            polynomials_multiplied[index] = polynomials_multiplied[index] + coefficient
    return polynomials_multiplied

def leading_term_index(polynomial):
    leading_term = 0
    for i in range(2*N):
        if polynomial[i] != 0:
            leading_term = i
    return leading_term

def reduce_polynomial(polynomial):
    current_lead = leading_term_index(polynomial)
    if current_lead < irreducible_leading_term_index:
        return polynomial

    if current_lead >= irreducible_leading_term_index:
        factor = polynomial[current_lead]
        index_shift = current_lead - irreducible_leading_term_index

        shifted_scaled_irreducible = [0 for i in range(2*N)]
        for i in range(irreducible_leading_term_index+1):
            shifted_scaled_irreducible[i + index_shift] = factor * fixed_irreducible_polynomial[i]

        next_stage_reduction = [polynomial[i] - shifted_scaled_irreducible[i] for i in range(2*N)]

        return reduce_polynomial(next_stage_reduction)

    else:
        return polynomial

print("-----------------------")
print("Finite Field Arithmetic")
print("-----------------------\n")

print("polynomial_0 :\nP(x) = " + to_human_readable(polynomial_0), "\nP(1,0) : " + str(polynomial_0) + "\n")
print("polynomial_1 :\nP(x) = " + to_human_readable(polynomial_1), "\nP(1,0) : " + str(polynomial_1) + "\n")
print("fixed_irreducible_polynomial: \nI(x) = " + str(to_human_readable(fixed_irreducible_polynomial)), "\nGF_I(1,0) : " + str(fixed_irreducible_polynomial) + "\n")

add_polys = add_polynomials(polynomial_0, polynomial_1)
convert_human_add = to_human_readable(add_polys)
print("polynomial_0 + polynomial_1 :\nP(x) = "  + str(convert_human_add) + "\nP(1,0) : " + str(add_polys) + "\n")

multiply_polys = multiply_polynomials(polynomial_0, polynomial_1)
reduced_poly = reduce_polynomial(multiply_polys)
convert_human_reduced = to_human_readable(reduced_poly)
print("(polynomial_0 * polynomial_1) % fixed_irreducible_polynomial :\nGF(x) = "  + str(convert_human_reduced) + "\nGF(1,0) : " + str(reduced_poly) + "\n")

print("-----------------------")
print("-----------------------\n")