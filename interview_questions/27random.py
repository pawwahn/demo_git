import random

print(random.random())  # random.random(): Returns a random float number between 0.0 and 1.0

print(random.uniform(2.5, 7.8)) #random.uniform(a, b): Returns a random float number between a and b

captcha = random.randint(10000,999999)
print(captcha)