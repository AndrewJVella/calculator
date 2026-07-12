
from math import *
def main():
	print("\nThis is a calculator, written in python.\nIt's like an online calculator tool, without silly click buttons;\nor like a search bar without nonsensical querey suggestions.\nYou can just use the shell, but this imports the math library and captures errors neatly.")
	print()
	print("a + b\tadds a and b")
	print("a - b\tsubtracts b from a")
	print("a * b\tmultiplies a and b")
	print("a ** b\tgets a to the power of b")
	print("a / b\tdivides a over b")
	print("a // b\ttakes the floor of a / b")
	print("a % b\ttakes the remainder of a / b")
	print()
	print("'&', '|', '~', '^' are bitwise operators: and, or, not, xor")
	print()
	print("(a + b) * c\tparentheses are evaluated first")
	print("round(a,x)\trounds a to place value x")
	print("floor(a)\ttakes floor of a")
	print("ceil(a)\t\ttakes ceiling of a")
	print("pow(a,b)\talso gets a to the power of b")
	print("sqrt(a)\t\tgets square root of a")
	print("log(a)\t\tgets log base 10 of a")
	print("\nPlease read the docs for the math library for more functions.")
	
	i = None
	while i != "":
		i=input("\nProvide an expression to evaluate.\n> ").lower().strip()
		try:
			print(eval(i))
		except ValueError:
			print("Invalid Expression")
		except ZeroDivisionError:
			print("Zero Division Error")
		except Exception:
			print("Error")
main()
