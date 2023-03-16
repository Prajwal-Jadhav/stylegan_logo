import cv2
import numpy as np
import os

# for fname in os.listdir("./data"):
#     img = cv2.imread(f'./data/{fname}', cv2.IMREAD_UNCHANGED)
#     channels = None
#     if img.ndim == 2:
#         channels = 1
#     if img.ndim == 3:
#         channels = img.shape[-1]
#     if channels and channels == 1:
#         print(fname)
#         img_r = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#         cv2.imwrite(f"./output/{fname}", img_r)


for fname in os.listdir("./data"):
    img = cv2.imread(f'./data/{fname}', cv2.IMREAD_UNCHANGED)

    if (img.shape[0] != img.shape[1]) or img.shape[0] != 128 or img.shape[1] != 128:
        print(fname, img.shape)
        # r_img = cv2.resize(img, (128, 128))

        # cv2.imwrite(f"output/{fname}", r_img)

