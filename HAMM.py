def ham(s1,s2):
    count = 0
    for i in range(0, len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count


with open('data.txt') as infile:
    data = infile.readlines()

s = data[0]
t = data[1]

print ham(s,t)
