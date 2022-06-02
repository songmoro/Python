from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt

def dftmatrix(Nfft=32,N=None):
    'construct DFT matrix'
    k= np.arange(Nfft)
    if N is None: N = Nfft
    n = np.arange(N)
    U = np.matrix(np.exp(1j* 2*np.pi/Nfft *k*n[:,None])) # use numpy broadcasting to create matrix
    return U/np.sqrt(Nfft)


U = dftmatrix(64,16)
x = np.ones((16,1))
X = U.H*x

fig,ax = plt.subplots()
fig.set_size_inches((8,4))
ax.set_aspect(0.8)
ax.grid()
ax.plot(np.arange(0,64)*2*np.pi/64.,abs(X),'o-')
ax.set_ylabel(r'$|X(\Omega)|$',fontsize=18)
ax.set_xticks([0, np.pi/2., np.pi, 3*np.pi/2,2*np.pi])
ax.set_xlabel(r'$\Omega$',fontsize=16)
ax.axis([0, 2*np.pi,0,2.1])
ax.set_xticklabels(['0',r'$\frac{\pi}{2}$', r'$\pi$',r'$\frac{3\pi}{2}$', r'$2\pi$'],
                   fontsize=18);
plt.tight_layout()
plt.show()