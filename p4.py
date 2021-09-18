# wapp to read a string and count
# number of vowels and consonants

s1 = input(" enter a string ")
vc, cc = 0, 0

for s in s1:
	if s.isalpha():
		if s in "AEIOUaeiou":
			vc = vc + 1
		else:
			cc = cc + 1
print(vc, cc)
