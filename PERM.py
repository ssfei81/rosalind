def perm(l):
    if len(l)==1:
        return [l]
    
    p = []
    for i in range(len(l)):
        p += [[l[i]] + j for j in perm(l[:i] + l[i+1:])]
    return p
        

with open('data.txt') as infile:
    data = infile.readlines()

n = int(data[0].split()[0])
list = range(1,n+1)


li = perm(list)

output = open('output.txt', 'w')

output.write(str(len(li))+'\n')


for i in li:
    tmp = ''
    for j in i:
        tmp += str(j)+" "
    output.write(tmp+'\n')
        
