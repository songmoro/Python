from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt

fs = 64 # sampling frequency
f = 10  # one signal
t = np.arange(0,1,1/fs) # time-domain samples
deltaf = 1/2. # second nearby frequency
x=np.cos(2*np.pi*f*t) + np.cos(2*np.pi*(f+deltaf)*t)

Nf = 64*2
fig,ax = plt.subplots(2,1,sharex=True,sharey=True)
fig.set_size_inches((8,4))

X = np.fft.fft(x,Nf)/np.sqrt(Nf)
ax[0].plot(np.linspace(0,fs,len(X)),abs(X),'-o',ms=3.)
ax[0].set_title(r'$N=%d$'%Nf,fontsize=18)
ax[0].set_ylabel(r'$|X(k)|$',fontsize=18)
ax[0].grid()

Nf = 64*4
X = np.fft.fft(x,Nf)/np.sqrt(Nf)
ax[1].plot(np.linspace(0,fs,len(X)),abs(X),'-o',ms=3.)
ax[1].set_title(r'$N=%d$'%Nf,fontsize=18)
ax[1].set_ylabel(r'$|X(k)|$',fontsize=18)
ax[1].set_xlabel('Frequency (Hz)',fontsize=18)
ax[1].set_xlim(xmax = fs/2)
ax[1].set_ylim(ymax=6)
ax[1].grid()

plt.tight_layout()
plt.show()
