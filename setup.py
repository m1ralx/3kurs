from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

setup(
    options={'py2exe': {'bundle_files': 1}},
    windows=[{'script': "lab1.py"}],
    zipfile=None,
)
