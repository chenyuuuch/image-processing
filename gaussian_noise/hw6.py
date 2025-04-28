import numpy as np
import matplotlib.pyplot as plt

#建立 256x256 灰階值為 100 的影像
g = np.full((256, 256), 100, dtype=np.uint8)
#產生高斯雜訊
mean = 0
std_dev = 25
noise = np.random.normal(mean, std_dev, g.shape)
#將雜訊加入原始影像並截斷到 [0, 255]
f = g + noise
f = np.clip(f, 0, 255).astype(np.uint8)

#顯示影像與直方圖
plt.figure(figsize=(12, 6))
#顯示g(x,y)
plt.subplot(2, 2, 1)
plt.imshow(g, cmap='gray', vmin=0, vmax=255)
plt.title('Image g(x,y)')
plt.axis('off')
#顯示f(x,y)
plt.subplot(2, 2, 2)
plt.imshow(f, cmap='gray', vmin=0, vmax=255)
plt.title('Noisy Image f(x,y)')
plt.axis('off')
#g(x,y)的直方圖
plt.subplot(2, 2, 3)
plt.hist(g.ravel(), bins=256, range=[0, 256], color='gray')
plt.title('Histogram of g(x,y)')
#f(x,y)的直方圖
plt.subplot(2, 2, 4)
plt.hist(f.ravel(), bins=256, range=[0, 256], color='blue')
plt.title('Histogram of f(x,y)')
plt.tight_layout()
plt.show()