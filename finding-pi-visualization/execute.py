import numpy as np
import matplotlib.pyplot as plt

n = 10000                 # Increase the number of random points 'n' for achieving higher accuracy
x = np.random.rand(n,2)   # First row contains abscissa and Second row contains ordinate

inside_circle = x[np.sqrt(x[:,0]**2 + x[:,1]**2)<1]     # filter out points that lie inside the quarter circle
pi_value = 4*len(inside_circle)/len(x)                  # calcute value of PI
print("Estimated value of pi : {}" .format(pi_value))

# matplotlib code
plt.figure(figsize=(5,5))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Calculation of value of PI')

plt.scatter(x[:,0],x[:,1],s=1,c='red')
plt.scatter(inside_circle[:,0],inside_circle[:,1],s=1,c='blue')
plt.show()