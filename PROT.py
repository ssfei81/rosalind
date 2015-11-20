with open("tablePROT.txt", "r") as infile:
        data = infile.readlines()

table={}
for d in data:
    dsplit = d.split()
    for i in range(0,len(dsplit),2):
        table[dsplit[i]]=dsplit[i+1]


with open ("data.txt", "r") as infile:
    data = infile.readlines()

t = ''
str = data[0][:-1]
for i in range(0, len(str), 3):
    substr = str[i:i+3]
    if table[substr] == 'Stop':
        break 
    else:
        t+=table[substr]

print t

