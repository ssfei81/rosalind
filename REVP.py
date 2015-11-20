
def revc(str):
    reverse = str[::-1]
    output = ''
    for r in reverse:
        if r == 'A':
            output+='T'
        elif r == 'T':
            output += 'A'
        elif r == 'C':
            output += 'G'
        elif r == 'G':
            output += 'C'
    return output


with open ("data.txt", "r") as infile:
    data = infile.readlines()

data.pop(0)

dna = ''
for d in data:
    dna+=d[:-1]

for i,val in enumerate(dna):
    for j in range(4,13):
        subs = dna[i:i+j]
        if len(subs) ==j and (subs==revc(subs)):
            print i+1,j

