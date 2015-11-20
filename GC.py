start = 1
ID = []
DNAstrings = []
maxerror = 0
maxid = 0

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

print ID
print DNAstrings

for id, DNA in enumerate(DNAstrings):
    error = 100*(DNA.count('C') + DNA.count('G'))/float(len(DNA))
    if error > maxerror:
        maxerror = error
        maxid = id


print ID[maxid],maxerror
