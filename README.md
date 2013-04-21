Welcome to the Python course at IBM.

Installation
============

We will be using Python 2.7 along with these tools:

* The [IPython](http://ipython.org/) interactive environment
* The [pytest](http://pytest.org/) unit testing framework

Ubuntu Users
------------

1. Install the Python prerequisites:

<pre>
sudo apt-get install python-pip
sudo pip install ipython pytest
</pre>

1. Test if it works:

<pre>
ipython
</pre>

Windows Users
-------------

The easiest method is to install ActivePython with PyPM.

*Note: Even if you have a 64-bit version of Windows, please install the 32-bit version of ActivePython. 
The 64-bit version is known to be problematic.*

1. Install ActivePython from <http://www.activestate.com/activepython/downloads>
1. Open Windows command prompt, and then:

<pre>
pypm install pyreadline
pypm install ipython
pypm install pytest
</pre>

1. Test if it works by running IPython from the menu.


Editors / IDEs
--------------

* Most standard programmer's editors support Python out of the box: Vim, Emacs, Sublime etc.
* Eclipse supports Python with the [PyDev](http://pydev.org/) plugin. 
* You can also use the pre-packaged [Aptana Studio](http://www.aptana.com/) environment if you don't have Eclipse installed yet.

Resources
---------

* Python Documentation: http://docs.python.org/
* Python Package Index (PyPI): http://pypi.python.org/pypi
* Python static analysis tools: pyflakes (simple), pylint, pychecker


Configuring Tab Completion
--------------------------

<pre>
gavriep@gavriep-mac: -$ cat -/.pythonrc.py
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
gavriep@gavriep-mac: -$ echo $PYTHONSTARTUP
/Users/gavriep/.pythonrc.py
gavriep@gavriep-mac: -$
</pre>


*Have fun!*

Gavrie Philipson
