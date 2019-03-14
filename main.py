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

import numpy as np
#1
y = np.random.random(25)
#2
y=y.reshape(5,5)
print(y)
#3
y[:,4]=0
y[4,:]=0
print(y)
#4
y=y+5
print(y)
#5
print(np.any(y==6))
#6
x=np.random.random(25).reshape(5,5)
print("x\n",x)
print("x+y\n",(x+y))
print("x-y\n",(x-y))
#7
i=np.eye(4,3)
print(i)
b=np.ones((3,5), dtype=int)
b[:,2]=2
b[0,4]=6
print(b)
c=np.diag([1,2,3,4])
c=c+2
print(c)
#8
z=np.random.random_integers(0,30,4*4).reshape(4,4)
#z=np.random.randn(4,4)
z=np.sort(z, axis=None).reshape(4,4)
print(z)
#9
w=np.random.random_integers(1,10,30)
hi = np.argmax(np.bincount(w))
print(hi,"\n",w)
#10

w=np.where(w<3,0,w)
w=np.where(w>8,0,w)
print(w)
#11
jj=np.random.random_integers(-10,30,36).reshape(6,6)
je=np.extract(jj%3==0,jj)
print(jj,"\n",je)
#12

#13
print(np.roots([4,3,-4]))
print(np.roots([14,4,-4,2]))
#print(np.roots([1,0,-4]))
#14
day =np.arange("2019-03","2019-04",dtype=("datetime64[D]"))
print(day)
print(np.extract(np.is_busday(day),day))
