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

# def main(list_):
# 	result = list_spy([])

# 	for element in list_:
# 		i = bisect.bisect_right(list_, element)

# 		result.insert(i, element)

# 	return result

# if __name__ == "__main__":
# 	print("Main code called!")

# 	print(main([6, 5, 4, 3, 2, 1]))
