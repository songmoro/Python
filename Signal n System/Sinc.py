import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5,5,300) # redefine this here for convenience
fig = plt.figure()
ax = fig.add_subplot(111)
fs = 5.0 # sampling rate
ax.plot(t, np.sinc(fs * t))
ax.grid() # put gride on axes
ax.annotate("This keeps going...",
            xy = (-4,0),
            xytext = (-5+.1,0.5),
            arrowprops={'facecolor':'green',
                        'shrink':0.05},
            fontsize=14)
ax.annotate("... and going...",
            xy = (4,0),
            xytext = (3+.1,0.5),
            arrowprops={'facecolor':'green',
                        'shrink':0.05},
            fontsize=14)
plt.show()