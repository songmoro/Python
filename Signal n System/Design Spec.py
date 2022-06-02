from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

M, beta = signal.fir_filter_design.kaiserord(delta, (fstop-fpass)/(fs/2.0))

hn = signal.firwin(M,(fstop+fpass)/2.0, window = ('kaiser', beta), nyq = fs/2.0)
w,H = signal.freqz(hn)

fig, ax = subplots()
fig.set_size_inches((8, 3))

ax.plot(w/pi*fs/2.0, 20*log10(abs(H)))
ax.set_xlabel("Frequency (Hz)", fontsize = 16)
ax.set_ylabel(r"$20\log_{10} |H(f)| $", fontsize = 22)
ymin, ymax = -80, 5
ax.axis(ymin = ymin, ymax = ymax)
ax.add_patch(Rectangle((0, ymin), width = fpass, height = ymax-ymin, color = 'g', alpha = 0.3))
ax.add_patch(Rectangle((fpass, ymin), width = fstop-fpass, height = ymax-ymin, color = 'r', alpha = 0.3))
ax.add_patch(Rectangle((fstop, ymin), width = fs/2-fstop, height = ymax-ymin, color = 'y', alpha = 0.3))
ax.set_title("Number of taps=%d"%M)
ax.text(10, -15, 'passband', fontsize = 14, bbox = dict(color = 'white'))
ax.text(200, -15, 'stopband', fontsize = 16, bbox = dict(color = 'white'))
ax.grid()