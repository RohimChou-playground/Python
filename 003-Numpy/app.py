# =========================================================== #
# ======================= 0001.Hello World ======================= #
# =========================================================== #
import numpy as np

arr_0d = np.array(22)
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3 ], [4, 5, 6]]])
arr_random = np.array([[[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]])

print(type(arr_1d)) # <class 'numpy.ndarray'>
print("==================")
print(f"{arr_0d.ndim}d array")
print(arr_0d)
# ==================
# 0d array
# 22
print("==================")
print(f"{arr_1d.ndim}d array")
print(arr_1d)
# ==================
# 1d array
# [1 2 3 4 5]
print("==================")
print(f"{arr_2d.ndim}d array")
print(arr_2d)
# ==================
# 2d array
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print("==================")
print(f"{arr_3d.ndim}d array")
print(arr_3d)
# ==================
# 3d array
# [[[1 2 3]
#   [4 5 6]]
# 
#  [[1 2 3]
#   [4 5 6]]]
print("==================")
print(f"{arr_random.ndim}d array")
print(arr_random)
# ==================
# 1d array
# [list([[1, 2, 3], [4, 5, 6]]) list([1, 2, 3, 4, 5, 6])]










# =========================================================== #
# ======================= 0002.Index ======================= #
# =========================================================== #
print("\n\n======================= 0002.Index =======================")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr_2d[1, 2]) # 6

arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 22, 33], [44, 55, 66], [77, 88, 99]]])
print("==================")
print(arr_3d)
print(arr_3d[1, 2, 0]) 
# The first number represents the first dimension, which contains two arrays
# The second number represents the second dimension, which also contains three arrays
# The third number represents the third dimension, which contains three numbers
# ==================
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
# 
#  [[11 22 33]
#   [44 55 66]
#   [77 88 99]]]
# 77










# =========================================================== #
# ======================= 0003.copy vs view ======================= #
# =========================================================== #
print("\n\n======================= 0003.copy vs view =======================")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr_2d_cp = arr_2d.copy()
arr_2d_vw = arr_2d.view()
arr_2d[1, 2] = 999
print(arr_2d_cp)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(arr_2d_vw)
# [[  1   2   3]
#  [  4   5 999]
#  [  7   8   9]
#  [ 10  11  12]]










# =========================================================== #
# ======================= 0004.reshape ======================= #
# =========================================================== #
print("\n\n======================= 0004.reshape =======================")
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_2d = arr_1d.reshape(4, 3)
print(arr_2d)
print("==================")
arr_3d = arr_1d.reshape(2, 3, 2)
arr_1d[8] = 999
print(arr_3d)
# ==================
# [[[  1   2]
#   [  3   4]
#   [  5   6]]
# 
#  [[  7   8]
#   [999  10]
#   [ 11  12]]]
print("==================")
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_3d = arr_1d.reshape(2, 3, 2).copy()
arr_backto_1d = arr_3d.flatten()
print(arr_backto_1d)