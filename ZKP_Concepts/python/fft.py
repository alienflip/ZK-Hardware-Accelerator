'''
Computes the discrete fourier transform of a sequence

DFT : takes a sequence of complex numbers, x_n, and transforms them using : X_n = sum x_n.e^(-i.2.PI.k.n/N)

A widely used FFT implimentation is the 'Cooley-Turkey - radix-2 decimation-in-time FFT'

The idea here is to take advantage of the peridocity of the exponential term, recursively ...

Assumption : signal size of 2^n
'''

import random, math
PI = math.pi

## Example
N = 8
S = [random.randint(0, 9) for i in range(N)]
SIGNAL_IN = [[S[i], 0] for i in range(N)]
##

def fourier_exp(arg):
    return [math.cos(arg), -math.sin(arg)]

# DFT - O(n^2)

def DFT_Primitive(SIGNAL, k, N):
    real_term, imaginary_term = 0, 0
    for n in range(N):
        arg = 2*PI*k*n/N
        real_term = real_term + SIGNAL[n][0]*fourier_exp(arg)[0]
        imaginary_term = imaginary_term + SIGNAL[n][0]*fourier_exp(arg)[1]
    return [real_term, -imaginary_term]

def discrete_fourier_transform(SIGNAL):
    SIGNAL_OUT = []
    for k in range(N):
        SIGNAL_OUT.append(DFT_Primitive(SIGNAL, k, N))
    return SIGNAL_OUT

# FFT - O(nlog(n))

def complex_multiply(a, b):
    return [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]]

def fast_fourier_transform(SIGNAL):
    N = len(SIGNAL)
    R = int(N/2)
    
    if N == 1:
        return SIGNAL
    
    else:
        X_even = fast_fourier_transform(SIGNAL[::2])
        X_odd = fast_fourier_transform(SIGNAL[1::2])

        factors = [fourier_exp(-2*PI*i/N) for i in range(N)]

        out_low, out_high = [], []
        for i in range(R):
            _mult_out = complex_multiply(factors[:R][i], X_odd[i])
            out = [X_even[i][0]+_mult_out[0], X_even[i][1]+_mult_out[1]]
            out_low.append(out)
        for i in range(R):
            mult_out_ = complex_multiply(factors[R:][i], X_odd[i])
            out = [X_even[i][0]+mult_out_[0], X_even[i][1]+mult_out_[1]]
            out_high.append(out)
        return out_low + out_high


print("-----------------------------------------------------")
print("Discrete Fourier Transform and Fast Fourier Transform")
print("-----------------------------------------------------\n")

print("Input signal :\n" + "SIGNAL = " + str(SIGNAL_IN) + "\n")

print("DFT(SIGNAL) : \n" + str(discrete_fourier_transform(SIGNAL_IN)) + "\n")

print("FFT(SIGNAL) : \n" + str(fast_fourier_transform(SIGNAL_IN)) + "\n")

print("-----------------------------------------------------")
print("-----------------------------------------------------\n")
