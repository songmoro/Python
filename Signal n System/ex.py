import numpy as np
import matplotlib.pyplot as plt

# fig, ax = subplots() => fig, ax = plt.subplots()
# fig, axes = plt.subplots(2,2)
f = 1.0 # Hz, signal frequency
fs = 5.0 # Hz, sampling rate (ie. >=2*f)
# t = arange(-1,1+1/fs,1/fs) => t = np.arange(-1,1+1/fs,1/fs)
t = np.arange(-1,1+1/fs,1/fs) # sample interval, symmetric
                           # for convenence later
# x = sin(2*pi*f*t) => x = np.sin(2*np.pi*f*t)
x = np.sin(2*np.pi*f*t)
# ax.plot(t,x,'o-') => plt.plot(t,x,'o-')
plt.plot(t,x,'o-')
# ax.set_xlabel('Time', fontsize = 18) => plt.xlabel('Time', fontsize = 18)
plt.xlabel('Time', fontsize = 18)
plt.ylabel('Amplitude', fontsize = 18)
plt.show()

# fig, ax = subplots()
plt.plot(t, x, 'o-')
plt.axis(xmin = 1/(4*f)-1/fs*3,
        xmax = 1/(4*f)+1/fs*3,
        ymin = 0, ymax = 1.1 )
plt.xlabel('Time',fontsize=18)
plt.ylabel('Amplitude',fontsize=18)
plt.tight_layout()
plt.show()