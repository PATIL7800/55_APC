from array import array

a = array('u')

a.fromunicode("Hello")

print("Array:", a)
print("String:", a.tounicode())