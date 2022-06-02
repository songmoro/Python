import numpy as np
import matplotlib.pyplot as plt

fs = 5.0 # sampling rate
t = np.arange(-1,1+1/fs,0.001) # sample interval, symmetric
                              # for convenence later
k = np.array(sorted(set((t*fs).astype(int)))) # sorted coefficient list
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, (np.sin(2*np.pi*(k[:,None]/fs))*np.sinc(k[:,None]-fs*t)).T,'--',      #individual
        t,(np.sin(2*np.pi*(k[:,None]/fs))*np.sinc(k[:,None]-fs*t)).
        sum(axis=0),'k-') # whittaker interpolant k/fs

ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Amplitude', fontsize = 18)
ax.set_title('Sine Reconstructed with Whittaker Interpolator')
ax.axis((-1.1,1.1,-1.1,1.1))
plt.tight_layout()
plt.show()