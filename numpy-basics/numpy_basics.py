import numpy as np

# Scalar
scalar = np.array(5)
print("Scalar:", scalar)
print("Shape:", scalar.shape)

print()

# Vector
vector = np.array([10, 20, 30, 40])
print("Vector:", vector)
print("Shape:", vector.shape)

print()

# Matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matrix:")
print(matrix)
print("Shape:", matrix.shape)

print()

# Tensor (3D array)
tensor_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Tensor:")
print(tensor_3d)
print("Shape:", tensor_3d.shape)
