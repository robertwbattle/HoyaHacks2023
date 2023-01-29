import dataclasses
import collections
import inspect
import sys
import typing

@dataclasses.dataclass
class Invocation:
	initial_value: typing.Any
	operations: list[typing.Optional[tuple[str, list[typing.Any], dict[str, typing.Any]]]] = \
		dataclasses.field(default_factory=list)

	def encoded(self):
		return {
			"initial_value": self.initial_value,
			"operations": list(map(list, self.operations))
		}

@dataclasses.dataclass
class DataStructure:
	name: str
	type_: typing.Any
	invocations: list[Invocation]

	def encoded(self):
		return {
			"name": self.name,
			"type": "dict" if self.type_ is dict else "list" if self.type_ is list else None,
			"invocations": [
				None if invocation is None else invocation.encoded()

				for invocation in self.invocations
			]
		}

class FunctionMicroscopic:
	class Result:
		def __init__(self):
			self._invocation_id = 0

			self._dss = {}

		def new_invocation(self):
			self._invocation_id += 1

			for ds in self._dss.values():
				if len(ds.invocations) < self._invocation_id:
					ds.invocations.append(None)

		def record_ds(self, name, type_, initial_value):
			invocation = Invocation(initial_value)

			if name in self._dss:
				self._dss[name].invocations.append(invocation)
			else:
				self._dss[name] = DataStructure(name, type_, [invocation])

		def record_operation(self, ds_name, operation_name, args, kwargs):
			self._dss[ds_name]\
				.invocations[self._invocation_id]\
				.operations\
				.append((operation_name, args, kwargs))

		def encoded(self, ds_count):
			return [ds.encoded() for ds in self._dss.values()]

	def __init__(self, spy):
		self._spy = spy
		self._last_ds_count = None

		self._result = self.__class__.Result()

	def run(self, function, args, kwargs):
		first_ds_id = self._spy.next_ds_id()

		local_persister = LocalPersister()

		rv = local_persister.binded(function)(*args, **kwargs)

		ds_names = {}

		for ds_id in range(first_ds_id, self._spy.next_ds_id()):
			ds = self._spy.pop_ds()
			ds.retire()

			for local_name, local_value in local_persister.locals.items():
				if local_value is ds:
					ds_names[ds_id] = local_name

					self._result.record_ds(
						local_name,
						ds.supertype(),
						ds.initial_value
					)

					break
			else:
				print("Couldn't identify a data structure's variable name.", file=sys.stderr)

				sys.exit(1)

		while (operation := self._spy.peek_operation()) is not None and operation[0] >= first_ds_id:
			self._spy.pop_operation()
			self._result.record_operation(ds_names[operation[0]], *operation[1:])

		self._result.new_invocation()

		return rv

	def encoded_result(self):
		return self._result.encoded(self._last_ds_count)

class LocalPersister:
	""" Borrowed from https://code.activestate.com/recipes/577283-decorator-to-expose-local-variables-of-a-function-/ """

	def __init__(self):
		self.locals = None

	def binded(self, function):
		def wrapper(*args, **kwargs):
			def tracer(frame, event, _):
				if event == "return":
					self.locals = frame.f_locals.copy()

			old_profile = sys.getprofile()

			sys.setprofile(tracer)

			try:
				rv = function(*args, **kwargs)
			finally:
				sys.setprofile(old_profile)

			return rv

		return wrapper
