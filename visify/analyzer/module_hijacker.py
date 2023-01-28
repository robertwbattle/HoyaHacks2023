import importlib
import inspect
import os
import runpy
import sys
from visify.analyzer import first_frame_in_module
from visify.analyzer.spy import ModuleSpy

class ModuleHijacker:
	def __init__(self, module_name, spy=None):
		self.module_name = module_name
		self.spy = spy

		self.decorators = {}

	@staticmethod
	def _generate_mock_name(value, callback):
		class MockName(str):
			def __hash__(self):
				return super().__hash__()

			def __eq__(self, operand):
				if not getattr(self, "callback_called", False):
					self.callback_called = True

					if not callback(self):
						self.callback_called = False

				return super().__eq__(operand)

		return MockName(value)

	def _imported_module(self):
		return importlib.import_module(self.module_name)

	def _inject_decorators(self, mock_name, spy=None):
		if (frame := first_frame_in_module(self.module_name)) is None:
			return False

		module = sys.modules[frame.f_globals["__name__"]]

		for function_name, decorator in self.decorators.items():
			setattr(module, function_name, decorator(getattr(module, function_name)))

		if spy is not None:
			spy.inject(module)

		return True

	def add_decorator(self, function_name, decorator):
		current_decorator = self.decorators.get(function_name, lambda function: function)

		self.decorators[function_name] = lambda function: decorator(current_decorator(function))

	def module_functions(self):
		module = self._imported_module()

		members = inspect.getmembers(module, inspect.isfunction)

		return [
			function_name

			for function_name, function in members
			if function.__module__ == module.__name__
		]

	def run(self):
		mock_name = self.__class__._generate_mock_name(
			"__main__",
			lambda mock_name: self._inject_decorators(mock_name, self.spy)
		)

		runpy.run_module(self.module_name, run_name=mock_name, alter_sys=True)

		if not mock_name.callback_called:
			print("Couldn't identify the stack frame of the monkey-patch module", file=sys.stderr)

			sys.exit(1)
