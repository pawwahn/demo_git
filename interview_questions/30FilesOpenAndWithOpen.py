
try:
    files = open('test.txt', 'r')
    content = files.read()
except FileNotFoundError:
    print("File is not found")
finally:
    print("working on the next block")
