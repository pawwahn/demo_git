from collections import defaultdict

dic = defaultdict(lambda :0)

dic['a'] = 10
dic['b'] = 10

print(dic['a'])

print(dic['z'])

print(dic)
print(type(dic))