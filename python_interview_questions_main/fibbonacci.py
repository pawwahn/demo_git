def fib(n):
    seq = [0,1]
    while len(seq) <n:
        seq.append(seq[-1] + seq[-2])
    print(seq)

fib(10)