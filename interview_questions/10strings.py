str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)  # Output: Hello World

str3 = (str1+' ') *  3
print(str3)

#Accessing Characters
print("---->", str1)
s = str1[2]
print(s)11

s = str1[2:5]
print(s)

encoded_str3 = str3.encode()
print(encoded_str3)
print(encoded_str3.decode())
