import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

img = plt.imread("profile_light.jpg").copy()
if img.dtype == np.uint8:
    img = img/255.0

h,w,c = img.shape
center = np.array([h//2 - 20, w//2])
rad = int(0.9 * center[1])

for i in tqdm(range(h)):
    for j in range(w):
        cur_pos = np.array([i,j])
        dis = cur_pos - center
        if np.dot(dis, dis) > rad * rad:
            img[i,j,:] = 1.0

img = img[center[0]-rad:center[0]+rad,center[1]-rad:center[1]+rad,:]
plt.imsave("circle_profile.jpg", img)
