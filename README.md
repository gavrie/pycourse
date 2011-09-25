Python Course
=============

Installation
------------

* Python 2.7: http://python.org/download/releases/2.7.2/
* IPython: http://ipython.org/download.html
* PyWin32: http://sourceforge.net/projects/pywin32/files/pywin32/

Resources
---------

* Python Challenge: http://www.pythonchallenge.com/
* Python Documentation: http://docs.python.org/
* Python Package Index (PyPI): http://pypi.python.org/pypi
* Python static analysis tools: pyflakes (simple), pylint, pychecker

Tab Completion
--------------

<pre>
gavriep@gavriep-mac: ~$ cat ~/.pythonrc.py 
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
gavriep@gavriep-mac: ~$ echo $PYTHONSTARTUP 
/Users/gavriep/.pythonrc.py
gavriep@gavriep-mac: ~$ 
</pre>


*Have fun!*

Ofer Koren<br>
Eli Golovinsky<br>
Gavrie Philipson<br>
