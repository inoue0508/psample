import numpy as np

#配列の作成
multipliedMatrix = np.array([[1,1,1],[1,1,1],[1,1,1]])
multiplyMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

#行列の積
result = np.dot(multipliedMatrix,multiplyMatrix)

print(result)