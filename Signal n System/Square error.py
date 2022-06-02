import numpy as np
import matplotlib.pyplot as plt

f = 1.0 # Hz, signal frequency
fs = 5.0 # Hz, sampling rate (ie. >=2*f)
# t = arange(-1,1+1/fs,1/fs) => t = np.arange(-1,1+1/fs,1/fs)
t = np.arange(-1,1+1/fs,1/fs) # sample interval, symmetric
                              # for convenence later
# x = sin(2*pi*f*t) => x = np.sin(2*np.pi*f*t)
x = np.sin(2*np.pi*f*t)
interval = [] # piecewise domains
apprx = [] # line on domains
# build up points *evenly* inside of intervals
# hstack => np.hstack
# linspace => np.linspace
tp = np.hstack([np.linspace(t[i],t[i+1],20,False) for i in range(len(t)-1)])
# construct arguments for piecewise
for i in range(len(t)-1):
    interval.append(np.logical_and((t[i]) <= tp, tp < t[i+1]))
    apprx.append((x[i+1]-x[i])/(t[i+1]-t[i])*(tp[interval[-1]]-t[i]) + x[i])
x_hat = np.piecewise(tp, interval, apprx) # piecewise linear approximation


# fig, ax1 = subplots()
fig = plt.figure()
ax1 = fig.add_subplot(111)
# fill in the difference between the interpolant and the sinc
ax1.fill_between(tp, x_hat,np.sin(2*np.pi*f*tp), facecolor='red', edgecolor = 'black')
ax1.set_xlabel('Time', fontsize = 18)
ax1.set_ylabel('Amplitude', fontsize = 18)
ax2 = ax1.twinx() # create clone of ax1
sqe = (x_hat-np.sin(2*np.pi*f*tp))**2 # compute squared-error
ax2.plot(tp, sqe, 'r')
ax2.axis(xmin=-1,ymax= sqe.max())
ax2.set_ylabel('Squared error', color = 'r', fontsize = 18)
ax1.set_title('Errors with Piecewise Linear Interpolant', fontsize = 18)
plt.tight_layout()
plt.show()