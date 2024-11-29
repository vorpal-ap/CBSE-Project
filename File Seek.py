'''
Print contents after seeking 10 bytes
'''


file = open('abc.txt', 'r')
pointer = file.tell()
print("Pointer is currently in position ", pointer)
file.seek(10)
print("Moved pointer by 10 bytes")
content = file.read()
print("Contents ---")
print(content)
