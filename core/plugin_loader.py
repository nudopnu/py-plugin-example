import os
import importlib
from . import plugin_registry 
from .plugin import PluginInterface

def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)

def load_from_dir(plugin_path: str):
    plugins = [p for p in os.listdir(plugin_path) if p.endswith(".py")]
    for plugin_name in plugins:
        plugin_name, ext = os.path.splitext(plugin_name)
        mod = import_module(f"plugins.{plugin_name}")
        plugin_registry.register(plugin_name, mod)