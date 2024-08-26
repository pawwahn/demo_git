s = 'apple'

#rev_s = s[::-1]
#print(rev_s)

rs=''
len_of_s = len(s)
for i in range(0,(len_of_s)):
    rs = s[i] + rs
    print(rs)