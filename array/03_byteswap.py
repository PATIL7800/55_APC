from array import array

a = array('i', [1, 2, 3])

print("Before byteswap:", a)

a.byteswap()

print("After byteswap:", a)