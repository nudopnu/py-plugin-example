from .plugin import PluginInterface


registered = {}

def register(plugin_name: str, plugin):
    registered[plugin_name] = plugin

def call(plugin: str):
    registered[plugin].func()