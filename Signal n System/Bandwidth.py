import numpy as np
import matplotlib.pyplot as plt
import signal

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set_size_inches((7, 3))

N = 512
w = signal.windows.hamming(Ns)
W = db20(w, N)

m = 10
p = np.polyfit(arange(m)/N*Ns, W[:m]-W[0]+3.01, 2)
width = np.roots(p)[0]*2

ax.plot(arange(N)/N*Ns, W-W[0])
ax.set_ylim(ymin = -10)
ax.set_xlim(xmax = 2)

ax.vlines(width/2, 0, -60, lw = 2.0, linestyle = '--',color = 'g')
ax.set_ylabel('dB', fontsize = 22)
ax.set_title(r'$ BW_{3dB}$=%3.2f bins'%width, fontsize = 18)
ax.set_xlabel(r'$\frac{N_s}{N} k$', fontsize = 22)
ax.annotate('', fontsize = 28, xy = (0. -3), xytext = (width/2, -3), arrowprops = dict(arrowstyle = "<->", lx = 3))
ax.annotate('', fontsize = 28, xy = (1.2, 0), xytext = (1.2, -3), arrowprops = dict(arrowstyle = "<->", lx = 3))
ax.hlines(-3, width/2, 2, linestyle = '--', color = 'g', lw = 2)
ax.text(width/2/4, -5, r'$\frac{BW_{3dB}}{2}$', fontsize = 22)
ax.text(1.3, -2, '-3 dB', fontsize = 18)