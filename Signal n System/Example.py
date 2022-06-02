from __future__ import  division
from matplotlib.patches import FancyArrow
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt

def dftmatrix(Nfft=32,N=None):
    'construct DFT matrix'
    k= np.arange(Nfft)
    if N is None: N = Nfft
    n = np.arange(N)
    U = np.matrix(np.exp(1j* 2*np.pi/Nfft *k*n[:,None])) # use numpy broadcasting to create matrix
    return U/np.sqrt(Nfft)

def facet_filled(x,alpha=0.5,color='b'):
    'construct 3D facet from adjacent points filled to zero'
    a,b=x
    a0= a*np.array([1,1,0])
    b0= b*np.array([1,1,0])
    ve = np.vstack([a,a0,b0,b])      # create closed polygon facet
    poly = Poly3DCollection([ve]) # create facet
    poly.set_alpha(alpha)
    poly.set_color(color)
    return poly


def drawDFTView(X, ax=None, fig=None):
    'above code as a function. Draws 3D diagram given DFT matrix'
    a = 2 * np.pi / len(X) * np.arange(len(X))
    d = np.vstack([np.cos(a), np.sin(a), np.array(abs(X)).flatten()]).T
    if ax is None and fig is None:
        fig = plt.figure()
        fig.set_size_inches(6, 6)

    if ax is None:  # add ax to existing figure
        ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.axis([-1, 1, -1, 1])
    ax.set_zlim([0, d[:, 2].max()])
    ax.set_aspect('auto')
    ax.view_init(azim=-30)
    a = FancyArrow(0, 0, 1, 0, width=0.02, length_includes_head=True)
    ax.add_patch(a)
    b = FancyArrow(0, 0, 0, 1, width=0.02, length_includes_head=True)
    ax.add_patch(b)
    art3d.patch_2d_to_3d(a)
    art3d.patch_2d_to_3d(b)
    # ax.set_xticks([])
    # ax.set_yticks([])
    # ax.set_zticks([])
    ax.axis('off')

    sl = [slice(i, i + 2) for i in range(d.shape[0] - 2)]  # collect neighboring points
    for s in sl:
        poly = facet_filled(d[s, :])
        ax.add_collection3d(poly)

    # edge polygons    
    ax.add_collection3d(facet_filled(d[[-1, 0], :]))
    ax.add_collection3d(facet_filled(d[[-2, -1], :]))


def drawInOut(X, v, return_axes=False):
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    gs = gridspec.GridSpec(8, 6)

    ax1 = plt.subplot(gs[3:5, :2])
    ax2 = plt.subplot(gs[:, 2:], projection='3d')

    ax1.stem(np.arange(len(v)), v)
    ymin, ymax = ax1.get_ylim()
    ax1.set_ylim(ymax=ymax * 1.2, ymin=ymin * 1.2)
    ax1.set_title('input signal')
    ax1.set_xlabel('time sample index')
    ax1.tick_params(labelsize=8)

    drawDFTView(X, ax2)
    if return_axes:
        return ax1, ax2

U = dftmatrix(64,16)
x = np.ones((16,1))
X = U.H*x

v = np.matrix(np.cos(np.pi*np.arange(0,16))).T
ax1,ax2=drawInOut(U.H*v,v,return_axes=1)
ax1.set_title('Highest Frequency')
# ax1.figure.savefig('figure_00@.png', bbox_inches='tight', dpi=300)
plt.tight_layout()
plt.show()
v = np.ones((16,1))
ax1,ax2=drawInOut(U.H*v,v,return_axes=1)
ax1.set_title('Lowest Frequency')
# ax1.figure.savefig('figure_00@.png', bbox_inches='tight', dpi=300)

plt.tight_layout()
plt.show()