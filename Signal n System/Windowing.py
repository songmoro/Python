from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

def abs_sinc(k=None,N=64,Ns=32):
    if k is None: k = np.arange(0,N-1)
    y = np.where(k == 0, 1.0e-20, k)
    return abs(np.sin( Ns*2*np.pi/N*y)/np.sin(2*np.pi*y/N))/np.sqrt(N)

def db20(W,Nfft=None):
    'Given DFT, return power level in dB'
    if Nfft is None: # assume W is DFT
        return 20*np.log10(abs(W))
    else: # assume time-domain passed, so need DFT
        return 20*np.log10(abs( np.fft.fft(W,Nfft)/np.sqrt(Nfft) ) )


fig,ax = plt.subplots()
fig.set_size_inches((8,3))

ax.plot(abs_sinc(N=512,Ns=10),label='duration=10')
ax.plot(abs_sinc(N=512,Ns=20),label='duration=20')
ax.set_xlabel('DFT Index',fontsize=18)
ax.set_ylabel(r'$|X(\Omega_k)|$',fontsize=18)
ax.set_title('Rectangular Windows DFTs',fontsize=18)
ax.grid()
ax.legend(loc=0);

plt.tight_layout()
plt.show()

fs = 64 # sampling frequency
t = np.arange(0,2,1/fs)
f = 10  # one signal
deltaf = 2.3 # second nearby frequency

Nf = 512
fig,ax = plt.subplots(3,1,sharex=True,sharey=True)
fig.set_size_inches((10,6))

x=np.cos(2*np.pi*f*t) + 10*np.cos(2*np.pi*(f+deltaf)*t)
X = np.fft.fft(x,Nf)/np.sqrt(Nf)
ax[0].plot(np.linspace(0,fs,len(X)),db20(X),'-o',ms=3.)
ax[0].set_xlim(xmax = fs/2)
ax[0].grid()
ax[0].text(0.5,0.5,'rectangular window',
                transform=ax[0].transAxes,
                backgroundcolor='lightyellow',
                fontsize=16)
ax[0].annotate('Smaller signal',
            fontsize=12,xy=(f,db20(X)[int(f/fs*Nf)]),
            xytext=(1,30),
            arrowprops={'facecolor':'m'})

w = scipy.signal.windows.triang(len(x))
X = np.fft.fft(x*w,Nf)/np.sqrt(Nf)
ax[1].plot(np.linspace(0,fs,len(X)),db20(X),'-o',ms=3.)
ax[1].set_xlim(xmax = fs/2)
ax[1].grid()
ax[1].text(0.5,0.5,'triangular window',
                transform=ax[1].transAxes,
                backgroundcolor='lightyellow',
                fontsize=16)
ax[1].annotate('Smaller signal',
            fontsize=12,xy=(f,db20(X)[int(f/fs*Nf)]),
            xytext=(1,30),
            arrowprops={'facecolor':'m'})

w = scipy.signal.windows.hamming(len(x))
X = np.fft.fft(x*w,Nf)/np.sqrt(Nf)
ax[2].plot(np.linspace(0,fs,len(X)),db20(X),'-o',ms=3.)
ax[2].set_xlabel('Frequency (Hz)',fontsize=18)
ax[2].set_xlim(xmax = fs/2)
ax[2].grid()
ax[2].set_ylim(ymin=-20)
ax[2].text(0.5,0.5,'Hamming window',
                transform=ax[2].transAxes,
                backgroundcolor='lightyellow',
                fontsize=16)
ax[2].annotate('Smaller signal',
            fontsize=12,xy=(f,db20(X)[int(f/fs*Nf)]),
            xytext=(1,30),
            arrowprops={'facecolor':'m'});
plt.tight_layout()
plt.show()
# fig.savefig('figure_00@.png', bbox_inches='tight', dpi=300)