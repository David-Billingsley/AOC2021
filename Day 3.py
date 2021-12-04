fdigit = []
sdigit = []
tdigit = []
fodigit = []
fidigit = []
intlist = []

with open('diag.txt') as f:
    for binary in f.readlines():
        fdigit.append(binary[0])
        sdigit.append(binary[1])
        tdigit.append(binary[2])
        fodigit.append(binary[3])
        fidigit.append(binary[4])
        intlist.append(int(binary,2))

mindig = []
maxdig = []

maxdig.append(max(set(fdigit), key= fdigit.count))
maxdig.append(max(set(fdigit), key= sdigit.count))
maxdig.append(max(set(fdigit), key= tdigit.count))
maxdig.append(max(set(fdigit), key= fodigit.count))
maxdig.append(max(set(fdigit), key= fidigit.count))

mindig.append(min(set(fdigit), key= fdigit.count))
mindig.append(min(set(fdigit), key= sdigit.count))
mindig.append(min(set(fdigit), key= tdigit.count))
mindig.append(min(set(fdigit), key= fodigit.count))
mindig.append(min(set(fdigit), key= fidigit.count))


print(int(''.join(mindig), 2) * int(''. join(maxdig), 2))
