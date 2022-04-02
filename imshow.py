#this function is used to display images
import numpy as np
import matplotlib.pyplot as plt
x = np.identity(10)
identity_matrix_image = plt.imshow(x,plt.show())
#now plot a diffrent matrix,with a diffrent color map
A = np.random.randn(10,10)
random_matrix_image = plt.imshow(A)
plt.show()