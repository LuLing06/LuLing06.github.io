import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("profile.jpg")/255.0
img = img * 1.25
img = np.clip(img, 0.0 ,1.0)
plt.imsave("profile_light.jpg", img)
