#!/usr/bin/env python
import fnmatch
import importlib
import importlib.util
import os
import sys

def gen_find(filename):
    for path, dir_list, file_list in os.walk('.'):
        for name in fnmatch.filter(file_list, filename):
            yield os.path.join(path, name)

def main(filename):

    modulename = filename.split('.')[0]
    script_name = modulename + '.py'
    executable = gen_find(script_name)

    if executable:
        spec = importlib.util.spec_from_file_location(modulename, executable.__next__())
        script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script)

        script.run()

if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("Параметры запуска скрипта: start.py <script_name>")
        exit()
    main(sys.argv[1])