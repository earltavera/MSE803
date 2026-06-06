import numpy as np

# Define Matrix A (Input) and Matrix B (Kernel)
A = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [10, 0, 11]
])

B = np.array([
    [5, 3],
    [9, 1]
])

# Output dimensions for a 'valid' operation
output_rows = A.shape[0] - B.shape[0] + 1
output_cols = A.shape[1] - B.shape[1] + 1

# ==========================================
# 1. Standard Convolution (Kernel is flipped)
# ==========================================
B_flipped = np.flip(B)
conv_result = np.zeros((output_rows, output_cols))

for i in range(output_rows):
    for j in range(output_cols):
        region = A[i : i + B.shape[0], j : j + B.shape[1]]
        conv_result[i, j] = np.sum(region * B_flipped)

# ==========================================
# 2. Cross-Correlation (Kernel is NOT flipped)
# ==========================================
corr_result = np.zeros((output_rows, output_cols))

for i in range(output_rows):
    for j in range(output_cols):
        region = A[i : i + B.shape[0], j : j + B.shape[1]]
        corr_result[i, j] = np.sum(region * B)

# ==========================================
# Display Results
# ==========================================
print("--- 2D Operations using Pure NumPy ---")
print("\nMatrix A:")
print(A)
print("\nMatrix B (Kernel):")
print(B)

print("\n1. Standard Convolution Result (Flipped Kernel):")
print(conv_result)

print("\n2. Cross-Correlation Result (Unflipped Kernel - Deep Learning standard):")
print(corr_result)