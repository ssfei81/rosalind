with open ("data.txt", "r") as myfile:
    data = myfile.readlines()

dna = data[0]

reverse = dna[::-1]

output = ''

for r in reverse:
    if r == 'A':
        output += 'T'
    elif r == 'T':
        output += 'A'
    elif r == 'C':
        output += 'G'
    elif r == 'G':
        output += 'C'

print output
