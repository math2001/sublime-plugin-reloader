# -*- encoding: utf-8 -*-

import os
import sys
import imp
import sublime_plugin


class ReloadPluginCommand(sublime_plugin.ApplicationCommand):

    """reload plugin, with all the files
    Example:
    sublime.run_command('matt_plugin_reloader', {
        'main': '.../Packages/example/main.py',
        'folders': ['matt'],
        'scripts': ['constants.py', 'hello.py']
    })
    Here, it will reload every file directly in 'matt', and the scripts 'constants.py'
    and 'hello.py'
    """

    def run(self, main, scripts=[], folders=[], times=2):

        base_path = os.path.dirname(main)
        pck_name = os.path.basename(base_path)
        for folder in folders:
            sys.path.append(os.path.join(base_path, folder))
            for item in os.listdir(os.path.join(base_path, folder)):
                root, ext = os.path.splitext(item)
                if (os.path.isfile(os.path.join(base_path, folder, item)) and
                        ext == '.py' and root != '__init__'):
                    module = '.'.join(
                        [pck_name, folder, os.path.splitext(item)[0]])
                    sublime_plugin.reload_plugin(module)
            sys.path.pop()
        for script in scripts:
            module = pck_name + '.' + \
                            (script[:-3] if script.endswith('.py') else script)
            sublime_plugin.reload_plugin(module)

        module = sys.modules[pck_name + '.' + os.path.splitext(
            os.path.basename(main))[0]]
        sublime_plugin.reload_plugin(module.__name__)
        if times > 1:
            return self.run(main, scripts, folders, times - 1)
