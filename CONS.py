start = 1
ID = []
DNAstrings = []

with open ("data.txt", "r") as infile:
    tmp = ''
    for line in infile:
        if line.startswith('>'):
            ID.append(line[1:])
            if(start):
                start = 0
            else:
                DNAstrings.append(tmp)
                tmp = ''
        else:
            tmp += line[:-1]
DNAstrings.append(tmp)

length = len(DNAstrings[0])

m = [0,0,0,0]
m[0] = [0]*length
m[1] = [0]*length
m[2] = [0]*length
m[3] = [0]*length

for i in range(0,length):
    for j in range(0, len(DNAstrings)):
        if DNAstrings[j][i] == 'A':
            m[0][i]+=1
        elif DNAstrings[j][i] == 'C':
            m[1][i]+=1
        elif DNAstrings[j][i] == 'G':
            m[2][i]+=1
        elif DNAstrings[j][i] == 'T':
            m[3][i]+=1

output=''

for i in range(0, len(DNAstrings[0])):
    l = [m[0][i], m[1][i], m[2][i], m[3][i]]

    maxindex = l.index(max(l))

    if maxindex == 0:
       output+='A'
    elif maxindex ==1:
        output+='C'
    elif maxindex==2:
        output+='G'
    elif maxindex==3:
        output+='T'

output+='\n'

for i in range(0,4):
    if i==0:
        output+="A: "
    elif i==1:
        output+="C: "
    elif i==2:
        output+="G: "
    elif i==3:
        output+="T: "

    for j in range(0, len(DNAstrings[0])):
        output+= str(m[i][j]) + " "
    output+="\n"

print output
