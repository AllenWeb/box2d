#!/usr/bin/env python

import sys
import os
import subprocess
import logging
from _tools import ClosureShared

js_path = "js"
closure_path = os.path.join('lib', 'closure-library','closure')
application_js_path = os.path.join(js_path, 'application.js')
js_dirs = map(lambda dir: os.path.join(js_path, dir), ['box2d','demo'])
closure_dependencies = js_dirs + [application_js_path]

# deps
calcdeps_py_path = os.path.join(closure_path, "bin", "calcdeps.py")
deps_js_path = os.path.join(js_path, "deps.js")

# compile
compiled_js_path = os.path.join(js_path, "compiled.js")
jar_path = os.path.join('_tools', 'closure_compiler', 'compiler.jar')
extern_dir = os.path.join(js_path, 'externs')

def make_deps():
  return ClosureShared.make_deps(calcdeps_py_path, deps_js_path, closure_path, closure_dependencies)

def compile(debug=False):
  js_files = ClosureShared.get_js_files_for_compile(application_js_path, deps_js_path, closure_path)
  
  extern_files = []
  for file in ClosureShared.find_files(extern_dir, '*.js'):
    extern_files.append(file)
  
  return ClosureShared.compile(jar_path, closure_path, js_files, extern_files, compiled_js_path, debug)

def print_help():
  return ClosureShared.print_help(jar_path)

if __name__ == '__main__':
  ClosureShared.run_command(make_deps())
  ClosureShared.run_command(compile())
