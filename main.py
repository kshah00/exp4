from add import *
from mul import *
from sub import *


a = int(input("Number 1: ")) 
b = int(input("Number 2: "))

cmd = input("CMD (+, -, *)")

if cmd == "+":
	print(add(a,b))
if cmd == "-":
	print(sub(a,b))
if cmd == "*":
	print(mul(a,b))


