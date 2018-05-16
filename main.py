from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


def get_contour_points(image_):
    points_ = []
    check = True

    for i in range(image_.shape[0]):
        for j in range(image_.shape[1]):
            if image_[i][j] != check and (i, j) not in points_:
                points_.append((i, j))
                check = not check
    for i in range(image_.shape[1]):
        for j in range(image_.shape[0]):
            if image_[j][i] != check and (j, i) not in points_:
                points_.append((j, i))
                check = not check
    return points_


image = io.imread("test.png")
image = rgb2gray(image)
image = image < 1

points = get_contour_points(image)
weight_point = (int((max(points, key=lambda t: t[0])[0] - min(points, key=lambda t: t[0])[0]) / 2),
                int((max(points, key=lambda t: t[1])[1] - min(points, key=lambda t: t[1])[1]) / 2))


plt.imshow(image, cmap="gray")
plt.axis("off")
plt.show()
