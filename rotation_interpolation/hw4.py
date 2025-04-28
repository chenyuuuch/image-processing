import cv2
import numpy as np

def create_image(size=(300, 300), square_size=100):
    image = np.zeros(size, dtype=np.uint8) #建立影像
    start = (size[0] - square_size) // 2 #置中
    end = start + square_size #結束位置
    image[start:end, start:end] = 255 #白色
    return image

def rotate_image(image, angle, interpolation):
    rows, cols = image.shape #取得寬高
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1) #取得矩陣
    return cv2.warpAffine(image, M, (cols, rows), flags=interpolation)

def main():
    image = create_image()
    
    nearest_rotated = rotate_image(image, 30, cv2.INTER_NEAREST)
    bilinear_rotated = rotate_image(image, 30, cv2.INTER_LINEAR)
    
    cv2.imwrite("original.jpg", image)
    cv2.imwrite("nearest_rotated.jpg", nearest_rotated)
    cv2.imwrite("bilinear_rotated.jpg", bilinear_rotated)
    
if __name__ == "__main__":
    main()