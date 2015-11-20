with open ("data.txt", "r") as myfile:
    data = myfile.readlines()

dna = data[0]

print dna.replace('T', 'U')
