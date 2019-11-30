import random

def power(a,n):
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = s*s
		else:
			s=s*s*a
	return s

def Ferm(p):
	for a in range(2,p):
		if power(a,p-1) % p != 1:
			return a
	return 1

#n = [random.randint(2,10000)]
n = range(2,10000)

for i in n:
	print(i,Ferm(i),sep = ' ',end = '|')
