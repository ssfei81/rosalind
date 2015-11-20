maxid = 0

with open ("data.txt", "r") as infile:
    data = infile.readlines()

s = data[0][:-1]
t = data[1][:-1]

output =''
for i in range(len(s)):
    if s.startswith(t,i):
        output += str(i+1)+' '

print output
