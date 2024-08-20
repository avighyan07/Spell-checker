import nbformat
from nbconvert import PythonExporter
import importlib.util
import sys

def import_notebook(nb_path):
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)

    exporter = PythonExporter()
    source, _ = exporter.from_notebook_node(nb)

    module_name = nb_path.replace('.ipynb', '')
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(source, module.__dict__)
    sys.modules[module_name] = module

    return module
