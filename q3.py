def sbox_1(input_bits):
 
   
    S1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    
    
    input_bits_str = ''.join(map(str, input_bits))
    
    
    row = int(input_bits_str[0] + input_bits_str[5], 2)  
    col = int(input_bits_str[1:5], 2) 
    
   
    sbox_value = S1[row][col]
    
    output_bits = list(map(int, format(sbox_value, '04b')))
    
    return output_bits


input_block = [1, 0, 1, 0, 1, 1]

output_block = sbox_1(input_block)
print("S-box 1 Output:")
print(output_block)


output_block_str = ''.join(map(str, output_block))
print("\nS-box 1 Output (as binary string):")
print(output_block_str)
