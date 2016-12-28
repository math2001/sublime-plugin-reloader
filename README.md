# Reload Plugin

Reload Plugin is a ... plugin that reloads your Sublime Text's plugins. As you probably know, Sublime Text doesn't load the `.py` files that are more than 2 folders deep (your package folder, if it's deeper, it's ignored).

## Usage

Just add a listener in your package:

```python
import sublime
import sublime_plugin
import os

class MyPluginDevListner(sublime_plugin.EventListner):

    def on_post_save(self, view):
        sublime.run_command('reload_plugin', {
            'main': os.path.join(sublime.packages_path(), 'MyPlugin',
                                 'MyPlugin.py')
            'scripts': ['functions.py'] # at the root of your plugin,
            'folders': ['my_plugin_commands'] # all the files will be relaoded
            'times': 2 # default value: 2
        })

```

It reloads everything twice to make sure that your dependencies are reloaded.
