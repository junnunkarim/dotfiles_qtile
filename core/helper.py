import importlib.util


# dynamically load module
def load_module(module_path):
    try:
        module = importlib.import_module(module_path)
        return module
    except ImportError:
        print("Error: Could not import module")
        return None
