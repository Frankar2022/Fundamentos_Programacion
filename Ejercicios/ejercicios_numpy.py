import numpy as np

# m1D = np.array([1,2,3,4,5])
# # print(m1D)

# m2D = np.array([[1,2,3,4],[6,7,8,9]])
# print(m2D)
# print(type(m2D))
# print(m2D.shape)
# print(m1D.shape)

# m3D = np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13]])

# print(m3D[2][0])

# mna = np.round(np.random.random((3,3)),2)
# print(mna)

# mne = np.random.randint(100,210,(3,3))
# print(mne)

# mceros = np.zeros((3,3))
# print(mceros)

# munos = np.ones((3,3))
# print(munos)

# mcte = np.full((3,3),5)
# print(mcte)

# mident = np.eye(3)
# print(mident)

mppal = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(mppal)
# print(mppal[1:3,0:2])

#print(np.fliplr(mppal))
# print(np.transpose(mppal))
# print(mppal.T)

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a)
# b = [0,2,0,1]
# print(a[np.arange(4),b])

# a = np.array([[1,2],[3,2],[4,5]])
# print(a)

# b = a > 2
# print(b)
# print(a[b])
# print(a[a > 2])

# x = np.array([1,2,3], dtype=np.int64)
# print(x.dtype)

a = np.array([[1,2],[3,4]])
b = np.array([[10,20],[30,40]])
# print(a+b)
# print(np.add(a,b))
# print(a-b)
# print(np.subtract(a,b))
# print(a*b)
# print(np.multiply(a,b))
# print(a/b)
# print(np.divide(a,b))

# print(np.sqrt(a))

# print(a+b)
print(np.dot(a,b))
print(np.matmul(a,b))