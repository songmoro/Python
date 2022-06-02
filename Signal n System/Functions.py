import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp

def kernel(x,sigma=1):
    'convenient function to compute kernel of eigenvalue problem'
    x = np.asanyarray(x) # ensure x is array
    y = np.pi*np.where(x == 0,1.0e-20, x) # avoid divide by zero
    return np.sin(sigma/2*y)/y

nstep = 100 # quick and dirty integral quantization
t = np.linspace(-1,1,nstep) # quantization of time
dt = np.diff(t)[0] # differential step size

sigma=3
w,v=sp.eigh(kernel(t-t[:,None],sigma))
maxv=v[:, w.argmax()]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,maxv)
ax.set_xlabel('time',fontsize=18)
ax.set_ylabel('$\psi_0(t)$',fontsize=22)
ax.set_title('Eigenvector corresponding to e-value=%3.4f;$\sigma$=%3.2f'%(w.max()*dt,sigma))

plt.tight_layout()
plt.show()

def kernel_tau(x,W=1):
    'convenient function to compute kernel of eigenvalue problem'
    x = np.asanyarray(x)
    y = np.pi*np.where(x == 0,1.0e-20, x)
    return np.sin(2*W*y)/y

nstep=300                # quick and dirty integral quantization
t = np.linspace(-1,1,nstep) # quantization of time
tt = np.linspace(-2,2,nstep)# extend interval

sigma = 5
W = sigma/2./2./t.max()

w,v=sp.eig(kernel_tau(t-tt[:,None],W))
ii = np.argsort(w.real)
maxv=v[:, w.real.argmax()].real
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tt,maxv/np.sign(maxv[nstep/2])) # normalize to keep orientation upwards
ax.set_xlabel('time',fontsize=14)
ax.set_ylabel(r'$\phi_{max}(t)$',fontsize=18)
ax.set_title('$\sigma=%d$'%(2*W*2*t.max()),fontsize=16)

plt.show()