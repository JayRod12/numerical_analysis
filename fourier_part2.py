from scipy import integrate
import math
import matplotlib.pyplot as plt
import numpy as np

# Function df/dx
df = lambda x : 2 * x

# Fourier series approximation to df/dx with n terms
def df_best_approx(x, n):
    val = 0.0
    for m in range(1, n + 1):
        val += ((-1) ** m) * math.sin(m * math.pi * x) / m
    val *= (-4) / math.pi
    return val

# Formula derived for ||f-fn*||^2
def difference_formula(n):
    res = float(8) / 3 
    val = 0.0
    for m in range(1, n + 1):
        val -= float(1) / (m ** 2)
    val *= 16 / (math.pi ** 2)
    return res + val

# Print integrals
print("Integral of df/dx = 2 * x", integrate.quad(df, -1, 1))
integrals = []
for i in range(9):
    # dfn*/dx
    dfn = lambda x : df_best_approx(x, i)
    # ||df/dx - dfn*/dx||^2 
    diff_sqred = lambda x : (df(x) - dfn(x)) ** 2
    integ = integrate.quad(diff_sqred, -1, 1)
    integrals.append(integ)
    res = difference_formula(i)
    #print("||df/dx - dfn*/dx||^2, n = {0}".format(i), integ)
    print("||f - fn*||^2, n = {0}".format(i))
    print("Integrating Numerically",integ)
    print("Derived formula        ", res)

plt.plot(range(1, 10), integrals)
plt.title('Approximating 2 * x')
plt.xlabel('Number of Fourier Terms')
plt.ylabel('Approximation Error')

# Vectorized version of function dfn*/dx
df_best_approx_vect = np.vectorize(df_best_approx)

# Plot f and fn
#plt.close('all')
_, axarr = plt.subplots(3, 3)

# Linear space to plot functions
x = np.linspace(-1, 1, 100)

n = 1
for i in range(3):
    for j in range(3):
        axarr[i][j].plot(x, df_best_approx_vect(x, n))
        axarr[i][j].plot(x, df(x))
        axarr[i][j].set_title('dfn*/dx, n = {0}'.format(n))
        n += 1

plt.show()



