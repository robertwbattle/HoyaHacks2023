from visify.analyzer.spy import dict_spy

def fizz():
	z = dict_spy({"cheese": 31313})
	z["pizz"] = 4729384972894

if __name__ == "__main__":
	fizz()