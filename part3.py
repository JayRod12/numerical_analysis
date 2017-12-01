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

# Show numerically ...

res = []
for n in range(1, 100):
    val = float(2 * n - 1) / (2 * n + 1)
    approx = df_best_approx(val, n)
    true = df(val)
    res.append(approx - true)
    
    
plt.plot(range(1, 100), res)
plt.title('dfn*(x) - df(x), x = (2n-1)/(2n+1)')
plt.xlabel('Number of Fourier Terms, n')
plt.ylabel('Difference')
plt.show()
