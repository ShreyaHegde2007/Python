import matplotlib.pyplot as plt
import numpy as np
x_points=np.array([1,2,3,4,5,6,7])
y_points=np.array([300,500,700,500,800,300,550])
plt.plot(x_points,y_points,"<:b",linestyle="dashed",mec="green",mfc="yellow",markersize=40)
plt.xlabel("days of the week")
plt.ylabel("calories burnt")
plt.show()
