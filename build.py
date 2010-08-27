#!/usr/bin/env python

import os
from _tools.Closure import Closure
from _tools import HtmlPost
from _tools.HtmlCompressor import HtmlCompressor

js_path = "js"
js_dirs = map(lambda dir: os.path.join(js_path, dir), ['box2d','demo'])
application_js_path = os.path.join(js_path, 'application.js')
deps_js_path = os.path.join(js_path, "deps.js")
compiled_js_path = os.path.join(js_path, "compiled.js")

closure = Closure(
  application_js_path = application_js_path,
  closure_dependencies = js_dirs + [application_js_path],
  deps_js_path = deps_js_path,
  compiled_js_path = compiled_js_path,
  extern_dir = os.path.join(js_path, 'externs')
)

closure.build_and_process('index.html', 'index_compiled.html')

compressor = HtmlCompressor('index_compiled.html', 'js/compressed.js', 'index_compressed.html')
compressor.compress()
