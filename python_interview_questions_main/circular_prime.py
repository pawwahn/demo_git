ls = [121,3,73]
new_ls = []

def reverse(n):
    if n>0:
        while n != 0:
            digit = n % 10
            value = digit * 10 + digit
            n = n//10
        ls.append(value)


reverse_num = 0


circular_prime = []

def is_prime(n):
    #print(n)
    if n>1:
        for i in range(2, (n//2)+1):
            if n % i == 0:
                break
        else:
            circular_prime.append(n)
    return circular_prime

for n in ls:
    #print("Present number is: ", n)
    final = is_prime(n)
print(final)
