Welcome to the Python course at IBM.

Installation
============

We will be using Python 2.7 along with these tools:

* The [IPython](http://ipython.org/) interactive environment
* The [pytest](http://pytest.org/) unit testing framework

Ubuntu Users
------------

* Install the Python prerequisites:

<pre>
sudo apt-get install python-pip
sudo pip install ipython pytest
</pre>

* Test if it works:

<pre>
ipython
</pre>

Windows Users
-------------

The easiest method is to install ActivePython with PyPM.

*Note: Even if you have a 64-bit version of Windows, please install the 32-bit version of ActivePython. 
The 64-bit version is known to be problematic.*

* Install ActivePython from <http://www.activestate.com/activepython/downloads>
* Open the Windows command prompt, and then:

<pre>
pypm -g install pyreadline
pypm -g install ipython
pypm -g install pytest
</pre>

* Test if it works by running IPython from the Windows menu or from the PyPM command prompt.


Editors / IDEs
--------------

* Most standard programmer's editors support Python out of the box: Vim, Emacs, Sublime etc.
* Eclipse supports Python with the [PyDev](http://pydev.org/) plugin. You can also use the pre-packaged [Aptana Studio](http://www.aptana.com/) environment if you don't have Eclipse installed yet.

Resources
---------

* Python booklet in Hebrew: http://cyber.org.il/python/python.pdf
* Python Documentation: http://docs.python.org/
* Python Tutorial: http://docs.python.org/2/tutorial/index.html
* Python Package Index (PyPI): http://pypi.python.org/pypi
* Python static analysis tools: pyflakes (simple), pylint, pychecker


Configuring Tab Completion
--------------------------

To get tab completion to work in the regular Python interactive shell,
add the following lines to the file `~/.pythonrc.py` (create it first if it doesn't exist):
<pre>
try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
</pre>

In addition, add the following line to your `~/.bashrc` file:
<pre>
export PYTHONSTARTUP=~/.pythonrc.py
</pre>



*Have fun!*

Gavrie Philipson
