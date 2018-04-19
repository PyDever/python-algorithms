
# simple unsigned sixteen bit integer in Python 3
def unsigned_16bit(n):
  return abs(n) & 0xFFFF
  
# to extend that to 32bit unsigned
def unsigned_32bit(n):
  return abs(n) & 0xFFFFFFFF
  
# signed 32bit value in Python 3
def signed_32bit(n):
  if abs(n) != n:
    return n & 0xFFFFFFFF
  else:
    return n & 0xFFFFFFFF
    
# unsigned simple character 
def unsigned_char(char):
  integer = ord(char)
  if abs(integer) != integer:
    pass
  else:
    return chr(integer & 0xFF)
    
    
