try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
    #print(locals())
finally:
    if 'non_existent_file.txt' in locals():
        'non_existent_file.txt'.close()
        print("File closed.")
