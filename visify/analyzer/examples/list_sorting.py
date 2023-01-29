import bisect
from visify.analyzer.spy import list_spy

def foo():
	x = list_spy(["Hello, world!"])

	bar()

def bar(recurse=False):
	if recurse:
		fizz()

		return

	y = list_spy(["Foo bar"])

	fizz()
	bar(True)

def fizz():
	z = list_spy([0])
	z.append(1)

if __name__ == "__main__":
	foo()
