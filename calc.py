
from math import *

def main():
	help()
	ans = None

	while ans != "":
		ans = input("\nProvide an expression to evaluate, (or type '?' for help):\n> ").lower().strip()
		if ans == "":
			print("Goodbye!")
			return
		if ans == "?":
			help()
			continue


		try:
			ans = eval(ans)

			if isinstance(ans, float):
				ans = round(ans, 6)
			
			if (ans) == int(ans):
				ans = int(ans)


			print(">", ans)
		except ValueError:
			print("> Value Error")
		except TypeError:
			print("> Type Error")
		except ZeroDivisionError:
			print("> Zero Division Error")
		except SyntaxError:
			print("> Syntax Error")
		except Exception:
			print("> Error")

def help():
	print("\nThis is a calculator. No clicking. No ads. No spam. \nPython3: MIT License. Use Ctrl+C to halt. Thanks!")
	print()
	print("a + b\tadds a and b")
	print("a - b\tsubtracts b from a")
	print("a * b\tmultiplies a and b")
	print("a ** b\tgets a to the power of b")
	print("a / b\tdivides a over b")
	print("a // b\tgets the floor of a / b")
	print("a % b\tgets the remainder of a / b")
	print()
	print("(a + b) * c\tparentheses are evaluated first")
	print("round(a,x)\trounds a to place value x")
	print("abs(a)\t\tgets absolute value of a")
	print("floor(a)\tgets floor of a")
	print("ceil(a)\t\tgets ceiling of a")
	print("sqrt(a)\t\tgets square root of a")
	print("log(a)\t\tgets natural log of a")
	print()
	print("Trigonometric functions are also supported")
	print("Constants: pi (3.1415), e (2.7182), tau (6.2831)")
	print("'&', '|', '~', '^' are bitwise operators: and, or, not, xor")



if __name__ == '__main__':
	main()
