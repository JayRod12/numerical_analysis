from scipy import integrate
import math
import matplotlib.pyplot as plt
import numpy as np

# Function f
f = lambda x : x**2

# Fourier series approximation to f with n terms
def f_best_approx(x, n):
    res = float(1) / 3
    val = 0.0
    for m in range(1, n + 1):
        val += ((-1) ** m) * math.cos(m * math.pi * x) / (m ** 2)
    val *= 4 / (math.pi ** 2)
    return res + val

# Formula derived for ||f-fn*||^2
def difference_formula(n):
    res = float(8) / 45 
    val = 0.0
    for m in range(1, n + 1):
        val -= float(1) / (m ** 4)
    val *= 16 / (math.pi ** 4)
    return res + val


integrals = []
for i in range(1, 10):
    # dfn*/dx
    fn = lambda x : f_best_approx(x, i)
    # (f - fn*)^2 
    diff_sqred = lambda x : (f(x) - fn(x)) ** 2
    # Compute using numerical integration
    integ = integrate.quad(diff_sqred, -1, 1)
    integrals.append(integ)
    # Compute using derived formula
    res = difference_formula(i)
    print("||f - fn*||^2, n = {0}".format(i))
    print("Integrating Numerically",integ)
    print("Derived formula        ", res)

# Plot integrals
plt.plot(range(1, 10), integrals)
plt.title('Approximating x^2')
plt.xlabel('Number of Fourier Terms')
plt.ylabel('Approximation Error')
    
## Plot f and fn
#plt.close('all')
_, axarr = plt.subplots(3, 3)

# Linear space to plot functions
x = np.linspace(-1, 1, 100)

# Vectorized version of function fn*
f_best_approx_vect = np.vectorize(f_best_approx)

n = 1
for i in range(3):
    for j in range(3):
        axarr[i][j].set_ylim([-0.1, 1])
        axarr[i][j].plot(x, f_best_approx_vect(x, n))
        axarr[i][j].plot(x, f(x))
        axarr[i][j].set_title('fn*, n = {0}'.format(n))
        n += 1

plt.show()



