from .plugin import PluginInterface


registered = {}

def register(plugin_name: str, plugin):
    registered[plugin_name] = plugin

def call(plugin: str):
    if plugin not in registered:
        raise ValueError(f"Plugin {plugin} not found")
    registered[plugin].func()