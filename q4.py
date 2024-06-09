
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]


PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]


SHIFT_SCHEDULE = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

def permute(original_key, permutation_table):
    return ''.join(original_key[i-1] for i in permutation_table)


def left_rotate(key, n):
    return key[n:] + key[:n]

def generate_subkeys(original_key):
  
    key_56bit = permute(original_key, PC1)
    
    
    left, right = key_56bit[:28], key_56bit[28:]
    
    subkeys = []
    for shift in SHIFT_SCHEDULE:
        
        left = left_rotate(left, shift)
        right = left_rotate(right, shift)
        
       
        combined = left + right
        subkey = permute(combined, PC2)
        
        subkeys.append(subkey)
        
    return subkeys


if __name__ == "__main__":
   
    original_key = '0001001100110100010101110111100110011011101111001101111111110001'
    
   
    subkeys = generate_subkeys(original_key)

    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1}: {subkey}")

