# Define the Initial Permutation (IP) Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Define the Final Permutation (FP) Table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

def permute(block, table):
    """Permute the block using the given table"""
    return [block[x - 1] for x in table]

def initial_permutation(block):
    """Apply Initial Permutation to the block"""
    return permute(block, IP)

def final_permutation(block):
    """Apply Final Permutation to the block"""
    return permute(block, FP)

# Example 64-bit block (in binary)
input_block = [1, 0, 1, 1, 0, 1, 0, 0,
               0, 1, 1, 0, 0, 1, 0, 1,
               1, 0, 1, 0, 1, 0, 1, 1,
               1, 1, 1, 1, 0, 0, 0, 0,
               0, 0, 0, 1, 1, 0, 1, 0,
               1, 0, 0, 1, 1, 1, 0, 0,
               0, 1, 1, 1, 0, 0, 1, 1,
               1, 0, 1, 0, 0, 1, 0, 0]

# Apply Initial Permutation
ip_block = initial_permutation(input_block)
print("Initial Permutation Output:")
print(ip_block)

# Apply Final Permutation
fp_block = final_permutation(ip_block)
print("\nFinal Permutation Output:")
print(fp_block)
