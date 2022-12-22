print('''
	Finding Cantor Digit

	Copyright by Sudiro

	email: Sudiro@mail.ugm.ac.id
	''')


import numpy as np
def f(n):
	if n <2:
		return 1
	else:
		return n*f(n-1)

def weight_sum(am):
	lam = len(am)
	sm = 0
	for m in range(1,lam+1):
		sm += am[m-1]*f(m)
	return sm

def find_cantor_digit(val):
	am = [1]
	while True:
		nf = f(len(am)+1)
		if(nf - val) < 0:
			am.append(len(am) + 1)
		else:
			break
	end_idx = -1
	while True:
		wsm = weight_sum(am)
		print("am: ", am, "\twsm: ", wsm, "\tval: ", val, "\terr: ", wsm - val, "\n")
		if(wsm - val) > 0:
			if am[end_idx] != 0:
				am[end_idx] -= 1
				wsm = weight_sum(am)
				if(wsm - val) < 0:
					am[end_idx] += 1
					end_idx -= 1
			else:
				if end_idx == -1:
					del am[end_idx]
				else:
					end_idx -= 1
		elif(wsm - val) == 0:
			break

val = 246531
find_cantor_digit(val)
print('---------------------\n')

val = 12345
find_cantor_digit(val)
print('---------------------\n')

val = 654321
find_cantor_digit(val)
print('---------------------\n')
