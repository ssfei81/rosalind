def seq(w,k):
    s = [1,1]
    if w==1 or w==2:
        return 1
    else:
        for i in range(2,w):
           s.append(s[i-1] + k*s[i-2])
        return s[w-1]



with open('data.txt') as infile:
    data = infile.readlines()

w,k = [int(x) for x in data[0].split()]

print seq(w,k)
