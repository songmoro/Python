from __future__ import  division

import matplotlib.patches
import mpl_toolkits.mplot3d.art3d
import numpy as np
import matplotlib.pyplot as plt


def dftmatrix(Nfft=32,N=None):
    'construct DFT matrix'
    k= np.arange(Nfft)
    if N is None: N = Nfft
    n = np.arange(N)
    U = np.matrix(np.exp(1j* 2*np.pi/Nfft *k*n[:,None])) # use numpy broadcasting to create matrix
    return U/np.sqrt(Nfft)

U = dftmatrix(64,16)
x = np.ones((16,1))
X = U.H*x

a = 2 * np.pi / 64. * np.arange(64)
d = np.vstack([np.cos(a), np.sin(a), np.array(abs(X)).flatten()]).T

fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.axis([-1, 1, -1, 1])
ax.set_zlim([0, d[:, 2].max()])
ax.set_aspect('auto')
ax.view_init(azim=-30)

ax.set_xlabel('real')
ax.set_ylabel('imag')
ax.set_zlabel('Abs')
ax.set_title('64-Point DFT Magnitudes')


def facet_filled(x, alpha=0.5, color='b'):
    'construct 3D facet from adjacent points filled to zero'
    a, b = x
    a0 = a * np.array([1, 1, 0])
    b0 = b * np.array([1, 1, 0])
    ve = np.vstack([a, a0, b0, b])  # create closed polygon facet
    poly = mpl_toolkits.mplot3d.art3d.Poly3DCollection([ve])  # create facet
    poly.set_alpha(alpha)
    poly.set_color(color)
    return poly


sl = [slice(i, i + 2) for i in range(d.shape[0] - 2)]  # collect neighboring points
for s in sl:
    poly = facet_filled(d[s, :])
    ax.add_collection3d(poly)

# edge polygons
ax.add_collection3d(facet_filled(d[[-1, 0], :]))
ax.add_collection3d(facet_filled(d[[-2, -1], :]))

# add 0 and pi/2 arrows for reference
a = matplotlib.patches.FancyArrow(0, 0, 1, 0, width=0.02, length_includes_head=True)
ax.add_patch(a)
b = matplotlib.patches.FancyArrow(0, 0, 0, 1, width=0.02, length_includes_head=True)
ax.add_patch(b)
mpl_toolkits.mplot3d.art3d.patch_2d_to_3d(a)
mpl_toolkits.mplot3d.art3d.patch_2d_to_3d(b)

plt.tight_layout()
plt.show()