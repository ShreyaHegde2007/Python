import matplotlib.pyplot as plt
import numpy as np
# plot1:
x=np.array([1,2,3,4,5,6])
y=np.array([2,4,6,8,10,12])
plt.subplot(1,2,2)
plt.plot(x,y)
# plot2:
x=np.array([3,6,9,12,15,18])
y=np.array([4,8,12,16,20,24])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()