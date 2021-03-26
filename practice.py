file=open('sandesh.txt', 'w')
l=['dog','cat', 'man', 'woman']

for nams in l:
    file.writelines(nams)

file.close()

with open('sandesh.txt', 'r') as f:
    print(f.readlines())
f.close()