f = [x for  x in range(1000000)]
print(f)

k = open(r'e.txt','w',errors='ignore')
for i in f:
    k.write(str(i)+'\n')
k.close()