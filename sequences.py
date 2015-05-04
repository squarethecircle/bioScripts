
import re

def addLines(lines):
	for line in lines:
		data=line.split()
		gind=data.pop(0)
		g_indices=re.split('[._]',gind)
		supercont='supercont10.'+g_indices[2]
		z_index=int(g_indices[3])-1
		for index, base in enumerate(data):
			sequences[indexes[index]][supercont][z_index] = base


def fastaIsEqual(f1,f2):
	trueFlag = True
	for s in f1.keys():
		if s not in f2.keys():
			return False
		a = str(f1[s])
		b = str(f2[s])
		if len(a) != len(b):
			return False
		for i,c in enumerate(a):
			if b[i] != c:
				trueFlag = False
				print (s,i,c,b[i])
	return trueFlag
