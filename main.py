from skimage import io
from skimage.color import rgb2gray
import math


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


def get_distances(points_, weight_point_):
    distances_ = []

    for point in points_:
        distances_.append(math.sqrt(math.fabs(
            ((point[0] - weight_point_[0]) ^ 2) + ((point[1] - weight_point_[1]) ^ 2))))
    return distances_


def get_haralick(distances_, length_):
    sum1 = 0
    sum2 = 0

    for distance in distances_:
        sum1 += distance
        sum2 += math.pow(distance, 2)

    return math.sqrt((math.pow(sum1, 2)) / (length_ * sum2 - 1))


image = io.imread("test.png")
image = rgb2gray(image)
image = image < 1

points = get_contour_points(image)
weight_point = (int((max(points, key=lambda t: t[0])[0] - min(points, key=lambda t: t[0])[0]) / 2),
                int((max(points, key=lambda t: t[1])[1] - min(points, key=lambda t: t[1])[1]) / 2))
distances = get_distances(points, weight_point)
haralick = get_haralick(distances, len(points))
print("Współczynnik Haralicka: " + str(haralick))
