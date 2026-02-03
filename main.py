a = int(input("Number 1: ")) 
b = int(input("Number 2: "))

cmd = input("CMD (+, -, /, *)")

if cmd == "+":
	add(a,b)
if cmd == "-":
	sub(a,b)
if cmd == "*":
	mul(a,b)
if cmd == "/":
	div(a,b)


