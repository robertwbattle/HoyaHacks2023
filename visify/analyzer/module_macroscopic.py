import collections
from visify.analyzer.function_microscopic import FunctionMicroscopic
from visify.analyzer.module_hijacker import ModuleHijacker
from visify.analyzer.spy import ModuleSpy

class ModuleMacroscopic:
	class DirectedGraph:
		def __init__(self):
			self._edges = collections.defaultdict(set)

		def add_edge(self, source, destination):
			self._edges[source].add(destination)

		def encoded(self):
			return [
				[source, destination]

				for source, destinations in self._edges.items()
				for destination in destinations
			]

	def __init__(self, module_name):
		self._spy = ModuleSpy()
		self._hijacker = ModuleHijacker(module_name, spy=self._spy)

		self._stack = []
		self._execution_graph = self.__class__.DirectedGraph()
		self._execution_order = []

		self._functions = []
		self._function_micros = {}

		for function_name in self._hijacker.module_functions():
			self._hijacker.add_decorator(function_name, self._decorator_factory(function_name))

			self._functions.append(function_name)
			self._function_micros[function_name] = FunctionMicroscopic(self._spy)

	def _decorator_factory(self, function_name):
		def decorator(function):
			def wrapper(*args, **kwargs):
				if len(self._stack) > 0:
					self._execution_graph.add_edge(self._stack[-1], function_name)

				self._stack.append(function_name)
				self._execution_order.append(function_name)

				order_len = len(self._execution_order)

				rv = self._function_micros[function_name].run(function, args, kwargs)

				del self._stack[-1]

				if len(self._execution_order) > order_len:
					self._execution_order.append(function_name)

				return rv

			return wrapper

		return decorator

	def _encoded_execution_graph(self):
		return self._execution_graph.encoded()

	def _encoded_execution_order(self):
		return self._execution_order.copy()

	def _encoded_function_micros(self):
		return {
			function_name: micro.encoded_result()

			for function_name, micro in self._function_micros.items()
		}

	def _encoded_functions(self):
		return self._functions.copy()

	def encoded_result(self):
		return {
			"functions": self._encoded_functions(),
			"edges": self._encoded_execution_graph(),
			"order": self._encoded_execution_order(),
			"microscopic": self._encoded_function_micros()
		}

	def run(self):
		self._hijacker.run()
