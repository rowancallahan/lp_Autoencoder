import matplotlib.pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}
matplotlib.rc('font', **font)


p_values = [0., 0.04, 0.5, 1, 1.5, 2, 7, np.inf]
xx, yy = np.meshgrid(np.linspace(-3, 3, num=101), np.linspace(-3, 3, num=101))
fig, axes = plt.subplots(ncols=(len(p_values) + 1)// 2,
                     nrows=2, figsize=(14, 7))
for p, ax in zip(p_values, axes.flat):
    if p == 0:
        zz = (xx != 0).astype(int) + (yy != 0).astype(int)
        ax.imshow(zz, cmap='rainbow', extent=(xx.min(),xx.max(),yy.min(),yy.max()), aspect="auto")
    else:
        if np.isinf(p):
            zz = np.maximum(np.abs(xx),np.abs(yy))
        else:
            zz = ((np.abs((xx))**p) + (np.abs((yy))**p))**(1./p)
        ax.contourf(xx, yy, zz, 30, cmap='rainbow')
        ax.contour(xx,yy,zz, [1,2], colors='black', linewidths = 2) 
        ax.set_title("L_%.3f norm contour plot" % p)
plt.show()
