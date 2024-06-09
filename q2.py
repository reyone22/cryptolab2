
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

def permute(block, table):
    """Permute the block using the given table"""
    return [block[x - 1] for x in table]

def expansion_permutation(block):
    """Apply Expansion Permutation to the block"""
    return permute(block, E)


half_block = [0, 1, 1, 0, 1, 1, 0, 1,
              1, 0, 1, 0, 0, 1, 1, 1,
              0, 1, 1, 0, 0, 0, 1, 0,
              1, 1, 1, 0, 0, 1, 0, 1]

expanded_block = expansion_permutation(half_block)
print("Expansion Permutation Output:")
print(expanded_block)

expanded_block_str = ''.join(map(str, expanded_block))
print("\nExpansion Permutation Output (as binary string):")
print(expanded_block_str)
