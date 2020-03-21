import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

#화면에 텍스트 이미지 출력
print(digits.images[4])

plt.imshow(digits.images[4], cmap="Greys")
plt.show()