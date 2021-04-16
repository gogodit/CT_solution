def solution(brown, yellow):
	s= brown + yellow

	for i in range(s, 2, -1):
		if s % i == 0:
			a = s//i
			if yellow == (i-2)*(a-2):
				return [ i, a ]

##======================================

import math
def solution(brown, yellow):
	answer = []
for i in range(1, int(math.sprt(yellow))+1):
	if yellow % i == 0:
		if 2 * ( i + (yellow / i))+4 == brown:
			return [ int (yellow / i) + 2, i + 2]

##========================================

def solution (brown, ellow):
	for a in range(1, int(yellow**0.5 + 1):
		if yellow % a == 0:
			b = yellow // a
			if 2 * a + 2 * b + 4 = brown:
				return [ b + 2, a + 2]
