import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

parser = argparse.ArgumentParser(description='Crop for paper figure')
parser.add_argument('--file', type=str, help='input file name')
parser.add_argument('--ofile', type=str, help='output file name')
parser.add_argument('--x', type=float, default=0.5, help='x center')
parser.add_argument('--y', type=float, default=0.5, help='y center')
parser.add_argument('--resize', type=int, default=512, help='y center')
args = parser.parse_args()
print(args)

x = args.x
y = args.y
f = args.file
of = args.ofile
resize = args.resize
size = 256

img = plt.imread(f)
h,w,c = img.shape
# import pdb; pdb.set_trace()
if h < w:
    resize_w = int(w * resize / h)
    resize_h = resize
else:
    resize_w = resize
    resize_h = int(h * resize / w)

img = cv2.resize(img, (resize_w, resize_h))
h,w,c = img.shape
x_p = int(x * w)
y_p = int(y * h)

img = img[y_p-size//2:y_p+size//2, x_p-size//2:x_p+size//2,:]
plt.imsave(of + ".png", img)



