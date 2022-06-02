import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

def db20(W,Nfft=None):
    'Given DFT, return power level in dB or take DFT if need be'
    assert  np.isscalar(W) or W.ndim==1
    if Nfft is None: # assume W is DFT
        return 20*np.log10(abs(W))

    else:  # assume time-domain passed, so need DFT
        DFT = np.fft.fft(np.array(W).flatten(), Nfft) / np.sqrt(Nfft)
        return 20 * np.log10(abs(DFT.flatten()))

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set_size_inches((6, 3))

Ns = 16
Nf = 256*2
freqs = np.arange(Nf)*2*np.pi/Nf
w = scipy.signal.windows.hann(Ns, False)
W = db20(w, Nf)

ax.plot(freqs, W, '-b', ms = 4.0)
ax.set_ylim(ymin = -60)
ax.set_xlim(xmax = np.pi*1.01)
ax.set_xlabel(r'$\omega$', fontsize = 14)
ax.set_ylabel(r'$20\log_{10}|W(\omega)|$', fontsize = 18)
ax.grid()
ax.set_title('Hanning Window', fontsize = 18)
plt.annotate('', fontsize = 28,
             xy =(76/Nf*2*np.pi, W[0]),xytext = (76/Nf*2*np.pi, W[0]-32),
             arrowprops = {'facecolor':'b', 'arrowstyle':'<->'})
ax.text(0.4, 0.5, 'Peek sidelobe level',
           fontsize = 18, transform = ax.transAxes,
        bbox = {'fc':'y', 'alpha':0.3})
