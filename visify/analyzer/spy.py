import inspect

class ModuleSpy:
	def __init__(self):
		self._dss = []

		self.operation_stack = []

	def inject(self, module):
		module._spy = self

	@staticmethod
	def operation_recorder(ds_id, operation_name):
		def decorator(operation):
			def wrapper(self, *args, **kwargs):
				_injected_module_spy().record_operation(
					ds_id,
					operation_name,
					args,
					kwargs
				)

				return operation(self, *args, **kwargs)

			return wrapper

		return decorator

	def add_ds(self, ds):
		self._dss.append(ds)

	def next_ds_id(self):
		return len(self._dss)

	def peek_operation(self):
		if len(self.operation_stack) > 0:
			return self.operation_stack[-1]

	def pop_ds(self):
		if len(self._dss) > 0:
			return self._dss.pop()

	def pop_operation(self):
		if len(self.operation_stack) > 0:
			return self.operation_stack.pop()

	def record_operation(self, ds_id, operation_name, args, kwargs):
		self.operation_stack.append((ds_id, operation_name, args, kwargs))

def _injected_module_spy():
	for frame_info in inspect.stack():
		globals_ = frame_info.frame.f_globals

		if "_spy" in globals_:
			return globals_["_spy"]

	return inspect.currentframe().f_globals["_spy"]

def generic_spy(ds, operation_names):
	module_spy = _injected_module_spy()

	ds_id = module_spy.next_ds_id()

	class Spy(type(ds)):
		def __init__(self, value):
			super().__init__(value)

			self.initial_value = value.copy()

			self.is_recording = False

		def retire(self):
			for operation_name in operation_names:
				setattr(self.__class__, operation_name, getattr(type(ds), operation_name))

		def supertype(self):
			return type(self.initial_value)
	
	def _monkey_patch_operation(operation_name):
		def spy_operation(self, *args, **kwargs):
			operation = getattr(type(ds), operation_name)

			if not self.is_recording:
				operation = ModuleSpy.operation_recorder(ds_id, operation_name)(operation)

			was_recording = self.is_recording

			self.is_recording = True

			rv = operation(self, *args, **kwargs)

			if not was_recording:
				self.is_recording = False

			return rv

		setattr(Spy, operation_name, spy_operation)

	for operation_name in operation_names:
		_monkey_patch_operation(operation_name)

	spy = Spy(ds)

	module_spy.add_ds(spy)

	return spy

def dict_spy(dict_):
	return generic_spy(dict_, ["__delitem__", "__setitem__"])

def list_spy(list_):
	return generic_spy(list_, ["__delitem__", "__setitem__", "append", "insert"])