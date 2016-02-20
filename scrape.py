k={}
i=0
with open('data1.txt') as fin:
	for line in fin:
		j=[]
		j = list(map(str,line.split(',')))
		k[j[0]] = [float(j[z]) for z in range(1,11)]
print(k)