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

def primdiv(n):
	res = []
	i = 2
	while i <= n:
		if n % i == 0:
			while n % i == 0:
				n//=i
			res.append(i)
		i += 1
	return res

def eiler(n):
	p = primdiv(n)
	p = list(map(lambda x: 1 - (1/x), p))
	for i in p:
		n = n * i
	return int(n)
	
def NOD(a,b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
def NOD2(a,b):
	u0 = 1
	v0 = 0
	u1 = 0
	v1 = 1
	while 1 > 0:
		q = a // b
		
		c = a
		a = b
		b = c % b
		
		c = u0
		u0 = u1
		u1 = c - q*u1
		
		c = v0
		v0 = v1
		v1 = c - q*v1
		
		if b == 0:
			return u0
	return u0

def fastpower_mod(a,n,b):
	a %= b
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = (s*s) % b
		else:
			s= (s*s*a) % b
	return s

def  rsa_encrypt(m, e, n):
	return fastpower_mod(m,e,n)

def decrypt(c, d, n):
	return fastpower_mod(c,d,n)

p = 13
q = 31
n = p*q
fi = (p - 1)*(q - 1)
e = 1
d = 0
for e in range(2,fi):
	if NOD(e,fi) == 1:
		d = NOD2(e,fi)
		break
print('e = {}\nn = {}\nф = {}\nd = {}'.format(e,n,fi,d))
m = int(input())
c = rsa_encrypt(m,e,n)
print(c)
print(decrypt(c, d, n))
	

