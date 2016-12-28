# -*- encoding: utf-8 -*-

import os
import sys
import imp
import sublime_plugin
from collections import namedtuple
from .matt.say_hello import SayHelloCommand


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

    def run(self, main, scripts=[], folders=[], first_call=True):

        base_path = os.path.dirname(main)
        pck_name = os.path.basename(base_path)
        for folder in folders:
            for item in os.listdir(os.path.join(base_path, folder)):
                root, ext = os.path.splitext(item)
                if (os.path.isfile(os.path.join(base_path, folder, item)) and
                        ext == '.py' and root != '__init__'):
                    module = '.'.join(
                        [pck_name, folder, os.path.splitext(item)[0]])
                    module = sys.modules.get(module, None)
                    if module is None:
                        continue
                    sublime_plugin.reload_plugin(module.__name__)
        for script in scripts:
            module = pck_name + '.' + os.path.splitext(script)[0]
            module = sys.modules.get(module, None)
            if module is None:
               continue
            sublime_plugin.reload_plugin(module.__name__)

        module = sys.modules[pck_name + '.' + os.path.splitext(
            os.path.basename(main))[0]]
        sublime_plugin.reload_plugin(module.__name__)
        if first_call:
            return self.run(main, scripts, folders, first_call=False)
