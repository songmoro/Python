from pylab import *
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

#fig, axs = subplots(2, 1, sharex = True)
fig = plt.figure()

plt.subplots_adjust(hspace = 0.2)
fig.set_size_inches((5, 5))

ax = fig.add_subplot(211)
w, h = signal.freqz([1/2.0, 1/2.0], 1)
ax.plot(w, 20*np.log10(abs(h)))
ax.set_ylabel(r"20 $\log_{10}$ $\|H$ ($\omega$)|", fontsize = 18)
ax.grid()

ax = fig.add_subplot(212)
ax.plot(w, np.angle(h, deg = True))
ax.set_xlabel(r'$\omega$', fontsize = 18)
ax.set_ylabel(r"$\phi$(deg)", fontsize = 18)
ax.set_xlim(xmax = np.pi)
ax.grid()

plt.tight_layout()
plt.show()