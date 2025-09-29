from core import plugin_loader, plugin_registry

plugin_loader.load_from_dir("plugins")
plugin_registry.call("test")