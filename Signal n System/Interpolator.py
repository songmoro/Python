import numpy as np
import matplotlib.pyplot as plt

#fig, ax = subplots()
fig = plt.figure()
ax = fig.add_subplot(111)

t = np.linspace(-1,1,100) # redefine this here for convenience
f = 1.0 # Hz, signal frequency
fs = 5.0 # Hz, sampling rate (ie. >=2*f)
ts = np.arange(-1,1+1/fs,1/fs) # sample points
num_coeffes = len(ts)
sm = 0
np.sinc
for k in range(-num_coeffes, num_coeffes): # since function is real, need both
    sm+= np.sin(2*np.pi*(k/fs))*np.sinc(k - fs*t)
ax.plot(t, sm, '--', t, np.sin(2*np.pi*t), ts, np.sin(2*np.pi*ts), 'o')
ax.set_title('Sampling Rate=%3.2f Hz' % fs, fontsize = 18)
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111)
# fill in the difference between the interpolant and the sinc
ax1.fill_between(t, sm, np.sin(2*np.pi*f*t), color='black')
ax1.set_xlabel('Time', fontsize = 18)
ax1.set_ylabel('Amplitude', fontsize = 18)
ax2 = ax1.twinx() # create clone of ax1
sqe = (sm-np.sin(2*np.pi*f*t))**2 # compute squared-error
ax2.plot(t, sqe, 'r')
ax2.axis(xmin=0,ymax= sqe.max())
ax2.set_ylabel('Squared error', color = 'r', fontsize = 18)
ax1.set_title(r'Errors with Whittaker Interpolant', fontsize = 18)
plt.tight_layout()
plt.show()
