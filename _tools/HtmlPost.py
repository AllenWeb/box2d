import sys
import os
import fnmatch
import string
import logging
import subprocess
import datetime
from xml.dom import minidom

def postProcess(source_html_file, target_html_file, source_js_files, compiled_js_file):
  dom = minidom.parse(source_html_file)
  script_elements = dom.getElementsByTagName('script')
  
  # remove all script references that are compiled
  for element in script_elements:
    process_script_element(element, source_js_files)
  
  # add in the compiled js file as the last element in 'head'
  blankTextElement = dom.createTextNode('')
  
  compiledElement = dom.createElement('script')
  compiledElement.setAttribute('src', compiled_js_file)
  compiledElement.appendChild(blankTextElement)
  
  head = dom.getElementsByTagName('head')[0]
  head.appendChild(compiledElement)
  fp = open(target_html_file,"w")
  dom.writexml(fp)

def process_script_element(element, source_js_files):
  if(element.hasAttribute('src')):
    src_attribute = element.getAttribute('src')
    if(source_js_files.count(src_attribute) > 0):
      element.parentNode.removeChild(element)
    else:
      blankElement = element.ownerDocument.createTextNode('')
      element.appendChild(blankElement)
  