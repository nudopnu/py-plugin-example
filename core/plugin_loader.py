import sys
import os
import importlib
from . import plugin_registry 
from .plugin import PluginInterface

def import_module(name: str) -> PluginInterface:
    print(f"importing {name}")
    return importlib.import_module(name)

def load_from_dir(plugin_dir: str):
    os.makedirs(plugin_dir, exist_ok=True)
    print(os.path.realpath(plugin_dir))
    sys.path.insert(0, os.path.realpath(plugin_dir))
    plugins = [p for p in os.listdir(plugin_dir) if p.endswith(".py")]
    for plugin_name in plugins:
        plugin_name, ext = os.path.splitext(plugin_name)
        mod = import_module(f"{plugin_name}")
        plugin_registry.register(plugin_name, mod)