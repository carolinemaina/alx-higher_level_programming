#!/usr/bin/python3
import importlib.util
import sys
if __name__ == "__main__":
    module_name = "hidden_4"
    module_spec = importlib.util.spec_from_file_location(module_name,
            "./hidden_4.pyc")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module_names = [name for name in dir(module) if not name.startswith("__")]
    module_names.sort()
    for name in module_names:
        print(name)
