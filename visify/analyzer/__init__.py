import importlib
import inspect
import os

def first_frame_in_module(module_name):
	module = importlib.import_module(module_name)
	module_path = os.path.abspath(module.__file__)

	for frame_info in inspect.stack():
		if os.path.abspath(frame_info.filename) == module_path:
			return frame_info.frame
