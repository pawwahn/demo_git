from collections import defaultdict

dic = defaultdict(lambda :0)

dic['a'] = 10
dic['b'] = 100

print(dic['a'])

print(dic['z'])

print(dict(dic))
print(type(dic))