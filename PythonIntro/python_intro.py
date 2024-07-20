# python_intro.py
"""Python Essentials: Introduction to Python.
<Name>
<Class>
<Date>
"""


if __name__ == "__main__":
	print("Hello, world!")


def sphere_volume(r):
	pi = 3.14159
	return (4/3) * pi * r**3

def isolate(a, b, c, d, e):
	
	print(a, b, sep='     ', end ='     ')
	print(c, d, e)

def first_half(s):
	return s[:int(len(s)/2)]

def backward(s):
	return s[::-1]

def list_ops():
	my_list = ["bear", "ant", "cat", "dog"]
	my_list.append("eagle")
	my_list.remove(my_list[2])
	my_list.insert(2, "fox")
	my_list.remove(my_list[1])
	my_list.sort()
	my_list.reverse()
	i = my_list.index("eagle")
	my_list.remove("eagle")
	my_list.insert(i, "hawk")
	my_list[-1] += "hunter"
	return my_list

def pig_latin(word):
	vowel = {'a', 'e', 'i', 'o', 'u'}
	if word[0] in vowel:
		return word + "hay"
	else: 
		return word[1:] + word[0] + "ay"

def palindrome():
	l = []
	for i in range(100, 1000):
		for j in range(100, 1000):
			s = str(i * j)
			if s == s[::-1]:
				l.append(int(s))

	return max(l)

def alt_harmonic(n):
	alt_harmonic_list = [((-1)**(i+1)/i) for i in range(1, n+1)]
	return sum(alt_harmonic_list)

	

