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

def average_df(x, n):
    val = 0.0
    for p in range(1, n + 1):
        val += df_best_approx(x, p)
    val /= (n + 1)
    return val

# Compare df with average dfn* for n = 1..9
_, ax = plt.subplots()

# Linear space
x = np.linspace(-1, 1, 100)

# Vectorized version of acerage_df
average_df_vect = np.vectorize(average_df)

# Legends
legend_funcs = []
legend_tags = []

# Plot df/dx
dff, = ax.plot(x, df(x))
legend_funcs.append(dff)
legend_tags.append('df/dx')
# Plot averages
for n in range(0, 10):
    ff, = ax.plot(x, average_df_vect(x, n))
    legend_funcs.append(ff)
    legend_tags.append('n = {0}'.format(n))

plt.legend(legend_funcs, legend_tags, loc=2)
plt.title('Average of derivatives from 1 to 9 vs df/dx')
plt.xlabel('x from -1 to 1')
plt.ylabel('Function values')
plt.show()
