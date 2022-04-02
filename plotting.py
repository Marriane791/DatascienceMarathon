import numpy as np
import matplotlib.pyplot as plt
#compute the parabola's x and y coordinates
x = np.arange(-5,5,0.1)
y = np.square(x)
#use matplotlib for the plot
plt.plot(x,y,'b')#specify the color blue for the line
plt.xlabel('x-Axis Values')
plt.ylabel('y-Axis Values')
plt.title('First Plot:A Parabola')
plt.show()#required to display the plot