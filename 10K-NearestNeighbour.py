import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

n = 50
trainData = np.random.randint(0, 100, [n, 2]).astype(np.float32)
color = np.random.randint(0, 2, n).astype(np.float32)
red = trainData[color == 1]
blue = trainData[color == 0]

plt.scatter(red[:, 0], red[:, 1], 100, 'r', '<')
plt.scatter(blue[:, 0], blue[:, 1], 100, 'b', '^')

newMember = np.random.randint(0, 100, [1, 2]).astype(np.float32)
plt.scatter(newMember[:, 0], newMember[:, 1], 100, 'g', 's')

knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, color)
ret, results, neighbours, dist = knn.findNearest(newMember, 3)
print("result:  {}\n".format(results))
print("neighbours:  {}\n".format(neighbours))
print("distance:  {}\n".format(dist))

plt.show()
