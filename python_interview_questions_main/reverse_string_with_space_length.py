s = 'apple banana'
# op = 'anana belppa'

new_s = s[::-1].replace(' ', '')
print(new_s)

word_split = s.split(' ')
word_length = [len(i) for i in word_split]
print(word_length)

s1 = ''
for i in new_s:
    for j in word_length:
        s1 = s1 + new_s[0:j] + ' '
        new_s = new_s[j:]
print(s1)
