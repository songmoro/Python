import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg


def kernel(x,sigma=1):
    'convenient function to compute kernel of eigenvalue problem'
    x = np.asanyarray(x) # ensure x is array
    y = np.pi*np.where(x == 0,1.0e-20, x) # avoid divide by zero
    return np.sin(sigma/2*y)/y

nstep = 100 # quick and dirty integral quantization
t = np.linspace(-1,1,nstep) # quantization of time
dt = np.diff(t)[0] # differential step size
def eigv(sigma):
    return scipy.linalg.eigvalsh(kernel(t-t[:,None],sigma)).max() # compute max eigenvalue

sigma = np.linspace(0.01,4,15) # range of time-bandwidth products to consider

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(sigma, dt*np.array([eigv(i) for i in sigma]),'-o')
ax.set_xlabel('time-bandwidth product $\sigma$',fontsize=14)
ax.set_ylabel('max eigenvalue',fontsize=14)
ax.axis(ymax=1.01)
ax.grid()
plt.tight_layout()
plt.show()