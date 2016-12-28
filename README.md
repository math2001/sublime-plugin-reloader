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
        if os.path.dirname(__file__) not in view.file_name():
            return
        sublime.run_command('reload_plugin', {
            'main': os.path.join(sublime.packages_path(), 'MyPlugin',
                                 'MyPlugin.py')
            'scripts': ['functions.py'] # at the root of your plugin,
            'folders': ['my_plugin_commands'] # all the files will be relaoded
            'times': 2 # default value: 2,
            'quiet': True # prevent default output in the console
        })

```

By default, it reloads everything twice to make sure that your dependencies are reloaded. If you have imported-importing-from-imported script or something a bit nested, you might want to increase it.

Note: The `.py` in the script name is optional.

A little tip: if you put this command in your main file, you can use the `__file__` variable (`'main': __file__`')

## Install

##### Using git

```bash
cd "%APPDATA%\Roaming\Sublime Text 3\Packages"     # on window
cd ~/Library/Application\ Support/Sublime\ Text\ 3 # on mac
cd ~/.config/sublime-text-3                        # on linux

git clone https://github.com/math2001/sublime-plugin-reloader reload_plugin
```

##### Using Package Control

Because it is not available on package control for now, you have to add this repo "manually" to your list.

1. Open up the command palette (`ctrl+shift+p`), and find `Package Control: Add Repository`. Then enter the URL of this repo: `https://github.com/math2001/reload_plugin` in the input field.
2. Open up the command palette again and find `Package Control: Install Package`, and just search for `reload_plugin`. (just a normal install)
