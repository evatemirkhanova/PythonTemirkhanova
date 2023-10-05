dec = int(input())
dec_oct = dec
dec_hex = dec

bin_sys = ''
while dec > 0:
    bin_sys += str(dec % 2)
    dec //= 2
    
oct_sys = ''
while dec_oct > 0:
    oct_sys += str(dec_oct % 8)
    dec_oct //= 8
 
hex_sys = ''
while dec_hex > 0:
    if dec_hex % 16 == 10:
        hex_sys += 'dec'
    elif dec_hex % 16 == 11:
        hex_sys += 'B'
    elif dec_hex % 16 == 12:
        hex_sys += 'C'
    elif dec_hex % 16 == 13:
        hex_sys += 'D'
    elif dec_hex % 16 == 14:
        hex_sys += 'E'
    elif dec_hex % 16 == 15:
        hex_sys += 'F'
    else:
        hex_sys += str(dec_hex % 16)
    dec_hex //= 16
    
binary = bin_sys[::-1]
octal = oct_sys[::-1]
hexadecimal = hex_sys[::-1]

print(binary, octal, hexadecimal, sep=', ')