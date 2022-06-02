from __future__ import division

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import subplots
from numpy import linspace, sin, pi, array, where, diff, argsort, sign
from numpy.linalg import eig, eigvalsh, eigh


def kernel(x,sigma=1):
    'convenient function to compute kernel of eigenvalue problem'
    x = np.asanyarray(x)
    y = pi*where(x == 0,1.0e-20, x)
    return sin(sigma/2*y)/y

nstep=100                # quick and dirty integral quantization
t = linspace(-1,1,nstep) # quantization of time
dt = diff(t)[0]          # differential step size
def eigv(sigma):
    return eigvalsh(kernel(t-t[:,None],sigma)).max() # compute max eigenvalue

sigma = linspace(0.01,4,15) # range of time-bandwidth products to consider

fig,ax = subplots()
ax.plot(sigma, dt*array([eigv(i) for i in sigma]),'-o')
ax.set_xlabel('time-bandwidth product $\sigma$',fontsize=14)
ax.set_ylabel('max eigenvalue',fontsize=14)
ax.axis(ymax=1.01)
ax.grid()

# fig.savefig('figure_00@.png', bbox_inches='tight', dpi=300)

sigma=3
w,v=eigh(kernel(t-t[:,None],sigma))
maxv=v[:, w.argmax()]
fig,ax=subplots()
ax.plot(t,maxv)
ax.set_xlabel('time',fontsize=14)
ax.set_title('Eigenvector corresponding to e-value=%2.4e;$\sigma$=%3.2f'%(w.max()*dt,sigma))

# fig.savefig('figure_00@.png', bbox_inches='tight', dpi=300)

plt.tight_layout()
plt.show()


def kernel_tau(x,W=1):
    'convenient function to compute kernel of eigenvalue problem'
    x = np.asanyarray(x)
    y = pi*where(x == 0,1.0e-20, x)
    return sin(2*W*y)/y

nstep=300                # quick and dirty integral quantization
t = linspace(-1,1,nstep) # quantization of time
tt = linspace(-2,2,nstep)# extend interval
sigma = 5
W = sigma/2./2./t.max()
w,v=eig(kernel_tau(t-tt[:,None],5))
ii = argsort(w.real)
maxv=v[:, w.real.argmax()].real
fig,ax = subplots()
ax.plot(tt,maxv)
##plot(tt,v[:,ii[-2]].real)
ax.set_xlabel('time',fontsize=14)
ax.set_title('$\sigma=%d$'%(2*W*2*t.max()),fontsize=16)

# fig.savefig('figure_00@.png', bbox_inches='tight', dpi=300)

plt.tight_layout()
plt.show()