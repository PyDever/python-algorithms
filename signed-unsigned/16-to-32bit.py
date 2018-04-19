def sign_extend(value, bits):
    highest_bit_mask = 1 << (bits - 1)
    remainder = 0
    for i in xrange(bits - 1):
        remainder = (remainder << 1) + 1

    if value & highest_bit_mask == highest_bit_mask:
        value = (value & remainder) - highest_bit_mask
    else:
        value = value & remainder
    return value
    
