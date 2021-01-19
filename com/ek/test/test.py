from com.ek.base.mhxy_server import MhxyServer

from PIL import Image, ImageEnhance
import pytesseract
import cv2 as cv


user_name_temp = '梦幻西游 ONLINE - ({}[{}] - {}[{}])'

# user_name = '梦幻西游 ONLINE - (山东1区[南天门] - 女。子。[23236601])'
user_name = user_name_temp.format('山东1区', '南天门', '女。子。', '23236601')

server1 = MhxyServer('山东1区', '南天门', '女。子。', '23236601')
print(server1.to_str())


# image = Image.open(r'E:\\22.png')
image31 = Image.open(r'E:\\31.png')
image311 = cv.imread(r'E:\\31.png', cv.IMREAD_GRAYSCALE)
image311 = cv.medianBlur(image311, 1)

# image311 = cv.cvtColor(image311, cv.COLOR_RGB2GRAY)
# image311 = cv.equalizeHist(image311)
# 全局阈值
# ret, img1 = cv.threshold(image311, 200, 255, cv.THRESH_BINARY)

# 自适应阈值
img1 = cv.adaptiveThreshold(image311, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 37, 1)

# 高斯滤波后采用Otsu阈值
# blur = cv.GaussianBlur(image311, (5, 5), 0)
# ret, img1 = cv.threshold(image311, 255, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imwrite('e:\\31-1.png', img1)

gray = cv.cvtColor(img1, cv.COLOR_BGR2BGRA)
# text = pytesseract.image_to_string(gray, lang='chi_sim')
# print(text)
print(image31.size)



