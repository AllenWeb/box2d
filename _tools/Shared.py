import os
import sys
import logging
import subprocess
import datetime
import fnmatch

def get_tmp_file_name(source_file_name):
  name = source_file_name
  name += "_tmp_"
  name += datetime.datetime.utcnow().isoformat().replace(':','_')
  return name

def run_command(command_func):
  logging.basicConfig(format='%(message)s', level=logging.INFO)
  args, tmp_file, out_file = command_func()
  logging.info('Running the following command: %s', ' '.join(args))
  proc = subprocess.Popen(args, stdout=subprocess.PIPE)
  (stdoutdata, stderrdata) = proc.communicate()
  if proc.returncode != 0:
    logging.error('Command failed.')
    sys.exit(1)
  else:
    sys.stdout.write(stdoutdata)
    logging.info('Command succeeded')
    logging.info("Moving temp file to '%s'", out_file)
    os.rename(tmp_file, out_file)

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename
