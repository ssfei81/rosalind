def mendel(k,m,n):
    prob = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1)); 
    return prob;

with open ("data.txt", "r") as infile:
    data = infile.readlines()

k,m,n = [int(i) for i in data[0].split()]

print mendel(k,m,n)

